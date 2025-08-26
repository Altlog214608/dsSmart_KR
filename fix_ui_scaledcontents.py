import os
import xml.etree.ElementTree as ET

def add_scaled_contents_to_ui(ui_path):
    """
    주어진 .ui XML 파일에서 모든 QLabel 위젯에
    scaledContents 프로퍼티를 true로 추가 또는 수정합니다.
    """
    tree = ET.parse(ui_path)
    root = tree.getroot()

    modified = False

    for widget in root.iter('widget'):
        if widget.attrib.get('class') == 'QLabel':
            # scaledContents 프로퍼티가 이미 있는지 확인
            has_scaled = False
            for prop in widget.findall('property'):
                if prop.attrib.get('name') == 'scaledContents':
                    has_scaled = True
                    bool_elem = prop.find('bool')
                    if bool_elem is not None and bool_elem.text.strip().lower() != 'true':
                        bool_elem.text = 'true'
                        modified = True
                    break
            # 없으면 새로 추가
            if not has_scaled:
                prop_scaled = ET.Element('property', {'name': 'scaledContents'})
                bool_elem = ET.SubElement(prop_scaled, 'bool')
                bool_elem.text = 'true'
                widget.append(prop_scaled)
                modified = True

    if modified:
        tree.write(ui_path, encoding='utf-8', xml_declaration=True)

def batch_process_ui_folder(ui_folder_path):
    """
    지정 폴더 내 모든 .ui 파일에 대해 add_scaled_contents_to_ui 실행
    """
    for foldername, subfolders, filenames in os.walk(ui_folder_path):
        for filename in filenames:
            if filename.endswith('.ui'):
                file_path = os.path.join(foldername, filename)
                print(f"Processing: {file_path}")
                add_scaled_contents_to_ui(file_path)

# 사용 예시: 현재 작업 폴더 내 ui 폴더 대상
ui_folder = './ui'
batch_process_ui_folder(ui_folder)
