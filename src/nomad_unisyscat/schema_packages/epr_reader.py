import struct


def parse_section(text, start_marker, end_marker):
    import re

    pattern = re.compile(
        rf'{re.escape(start_marker)}(.*?){re.escape(end_marker)}', re.DOTALL
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ''


def refined_parse_key_value_pairs(section_text):
    data = {}
    # Remove asterisks and leading/trailing whitespace
    clean_lines = [
        line.strip().replace('*', '')
        for line in section_text.split('\n')
        if line.strip() and not line.startswith('*')
    ]
    for line in clean_lines:
        if '=' in line:
            key, value = line.split('=', 1)
            data[key.strip()] = value.strip()
        elif '\t' in line:
            key, value = line.split('\t', 1)
            data[key.strip()] = value.strip()
        elif ' ' in line:
            key, value = line.split(' ', 1)
            data[key.strip()] = value.strip()
        elif line.startswith('.DVC'):
            key, value = line.split(' ', 1)
            data[key.strip('.DVC').strip()] = value.strip()
    return data


def generate_ydata_from_binary(inputfile):
    ydata = []
    with open(inputfile, 'rb') as file:
        indata = file.read()
    for i in range(0, len(indata), 8):
        pos = struct.unpack('>d', indata[i : i + 8])
        ydata.append(pos[0])
    return ydata


def generate_xdata_from_params(param_dict):
    xpoints = int(param_dict['XPTS'])
    xmin = float(param_dict['XMIN'])
    xwid = float(param_dict['XWID'])

    xmax = xmin + xwid
    xsampling = xwid / xpoints

    xdata = [xmin + (xsampling * i) for i in range(xpoints)]
    return xdata


def read_dsc_file(file_path):
    with open(file_path, 'r') as file:
        dsc_contents = file.read()
    return dsc_contents


def read_dta_file_full(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()

        data_dict = {
            'header_raw': binary_data[:128],  # First 128 bytes as raw header
            'data_points_raw': binary_data[128:],  # Remaining bytes as data points
        }

        try:
            data_dict['header_ascii'] = binary_data[:128].decode('ascii').strip()
        except UnicodeDecodeError:
            data_dict['header_ascii'] = None

        data_points_format = 'f' * (
            (len(binary_data) - 128) // 4
        )  # Assuming 4 bytes per float32
        try:
            data_dict['data_points_float'] = struct.unpack_from(
                data_points_format, binary_data, 128
            )
        except struct.error:
            data_dict['data_points_float'] = None

        return data_dict


def parse_dta_dsc(dta_file, dsc_file):
    dta_data = read_dta_file_full(dta_file)
    dsc_contents = read_dsc_file(dsc_file)

    desc_section = parse_section(dsc_contents, '#DESC', '#SPL')
    spl_section = parse_section(dsc_contents, '#SPL', '#DSL')
    dsl_section = parse_section(dsc_contents, '#DSL', '#MHL')
    mhl_section = parse_section(dsc_contents, '#MHL', '*')

    desc_data = refined_parse_key_value_pairs(desc_section)
    spl_data = refined_parse_key_value_pairs(spl_section)
    dsl_data = refined_parse_key_value_pairs(dsl_section)
    mhl_data = refined_parse_key_value_pairs(mhl_section)

    dta_ydata = generate_ydata_from_binary(dta_file)
    dta_xdata = generate_xdata_from_params(desc_data)

    if len(dta_ydata) != len(dta_xdata):
        dta_ydata = dta_ydata[: len(dta_xdata)]

    merged_data = {
        'header': dta_data['header_ascii'],
        'data_points': dta_data['data_points_float'],
        'descriptor_info': desc_data,
        'standard_parameters': spl_data,
        'device_specific': dsl_data,
        'manipulation_history': mhl_data,
        'x_values': dta_xdata,
        'y_values': dta_ydata,
    }

    return merged_data


# dta_file_path = '/home/pepe_marquez/NOMAD/nomad/plugins/nomad-unisyscat-plugin/tests/data/ReRH_Nia-C_H_EPR_exp_raw.DTA'
# dsc_file_path = '/mnt/data/ReRH_Nia-C_H_EPR_exp_raw.DSC'

# merged_data = parse_dta_dsc(dta_file_path, dsc_file_path)

# print(merged_data)

# # Save the merged data into a JSON file
# final_json_file_path = '/mnt/data/ReRH_Nia-C_H_EPR_exp_full_merged.json'
# with open(final_json_file_path, 'w') as json_file:
#     json.dump(merged_data, json_file)
