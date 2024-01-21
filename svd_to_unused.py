import xml.etree.ElementTree as ET
with open("/mnt/c/ST/STM32CubeIDE_1.14.1/STM32CubeIDE/plugins/com.st.stm32cube.ide.mcu.productdb.debug_2.1.100.202311191741/resources/cmsis/STMicroelectronics_CMSIS_SVD/STM32H745_CM7.svd") as f_in:
    tree = ET.parse(f_in)
    root = tree.getroot()
    periph_sizes = dict()
    for periph in root.find("peripherals").findall("peripheral"):
        name = periph.find("name").text
        if derived := periph.get("derivedFrom", False):
            size = periph_sizes[derived]
        else:
            size = periph.find("addressBlock").find("size").text
            periph_sizes[name] = size
        print(name, periph.find("baseAddress").text, size)