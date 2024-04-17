import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 1000
    height: 680
    visible: true
    Rectangle {
        id: bg
        color: "#e9ecef"
        anchors.fill: parent

        Rectangle {
            id: rectangle_header
            y: 16
            width: 936
            height: 84
            color: "#ffe3e3"
            radius: 8
            border.color: "#ffffff"
            border.width: 2
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter

            Text {
                id: header
                text: qsTr("🖥️ Matching Network Calculator")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 40
                font.bold: false
                font.family: "Tahoma"
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        Rectangle {
            id: retangle_choose_impedance
            x: 32
            y: 153
            width: 936
            height: 201
            color: "#ffffff"

            Image {
                id: image_l_section
                x: 16
                y: 8
                width: 239
                height: 147
                source: "image/L Section.jpg"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image_t_section
                x: 346
                y: 8
                width: 245
                height: 152
                source: "image/T Section.jpg"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image_pi_section
                x: 683
                y: 8
                width: 245
                height: 147
                source: "image/PI Section.jpg"
                fillMode: Image.PreserveAspectFit
            }

            RadioButton {
                id: radioButton_l_section
                x: 72
                y: 152
                text: qsTr("L Section")
                checked: backend.setData[6] == "L Section" ? true : false
                font.family: "Arial"
                font.pointSize: 15
                onClicked: {
                    backend.getTypeOfImpedance(radioButton_l_section.text)
                }
            }

            RadioButton {
                id: radioButton_t_section
                x: 404
                y: 152
                text: qsTr("T Section")
                checked: backend.setData[6] == "T Section" ? true : false
                font.family: "Arial"
                font.pointSize: 15
                onClicked: {
                    backend.getTypeOfImpedance(radioButton_t_section.text)
                }
            }

            RadioButton {
                id: radioButton_pi_section
                x: 738
                y: 152
                text: qsTr("PI Section")
                checked: backend.setData[6] == "PI Section" ? true : false
                font.family: "Arial"
                font.pointSize: 15
                onClicked: {
                    backend.getTypeOfImpedance(radioButton_pi_section.text)
                }
            }
        }

        Text {
            id: text_choose_impedance
            x: 32
            y: 113
            text: qsTr("I. Choose type of impedance matching network")
            font.pixelSize: 25
            font.family: "Arial"
        }

        Text {
            id: text_select_circuit
            x: 32
            y: 363
            text: qsTr("II. Select circuit type")
            font.pixelSize: 25
            font.family: "Arial"
        }

        RadioButton {
            id: radioButton_dc_feed
            x: 384
            y: 359
            text: qsTr("DC Feed")
            checked: backend.setData[7] == "DC Feed" ? true : false
            font.family: "Arial"
            font.pointSize: 15
            onClicked: {
                backend.getCircuitType(radioButton_dc_feed.text)
            }
        }

        RadioButton {
            id: radioButton_dc_block
            x: 644
            y: 360
            text: qsTr("DC Block")
            checked: backend.setData[7] == "DC Block" ? true : false
            font.family: "Arial"
            font.pointSize: 15
            onClicked: {
                backend.getCircuitType(radioButton_dc_block.text)
            }
        }

        Rectangle {
            id: rectangle_input_parameter
            x: 33
            y: 474
            width: 936
            height: 114
            color: "#ffffff"

            Text {
                id: text6
                x: 21
                y: 18
                text: qsTr("Source Resistance (Zs)")
                font.pixelSize: 22
                font.family: "Arial"
            }

            Rectangle {
                id: rectangle_zs_re
                x: 261
                width: 70
                height: 30
                color: "#ffffff"
                border.width: 1
                anchors.verticalCenter: text6.verticalCenter
                anchors.verticalCenterOffset: 0

                TextInput {
                    id: textInput_zs_re
                    text: backend.setData[0] == 0 ? "" : backend.setData[0]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
            }

            Text {
                id: text8
                x: 21
                y: 70
                text: qsTr("Load Resistance (Zl)")
                font.pixelSize: 22
                font.family: "Arial"
            }

            Rectangle {
                id: rectangle_zl_re
                x: 260
                y: 69
                width: 70
                height: 30
                color: "#ffffff"
                border.width: 1

                TextInput {
                    id: textInput_zl_re
                    text: backend.setData[2] == 0 ? "" : backend.setData[2]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
            }

            Text {
                id: text9
                x: 429
                y: 70
                text: qsTr("j Ω")
                font.pixelSize: 22
            }

            Text {
                id: text10
                x: 495
                y: 18
                text: qsTr("Frequency (f)")
                font.pixelSize: 22
                font.family: "Arial"
            }
            Rectangle {
                id: rectangle_f
                x: 688
                y: 16
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1

                TextInput {
                    id: textInput_f
                    text: backend.setData[4] == 0 ? "" : backend.setData[4]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
            }

            Text {
                id: text_quality_factor
                x: 495
                y: 70
                text: qsTr("Quality factor (Q)")
                font.pixelSize: 22
                font.family: "Arial"
                visible: radioButton_l_section.checked == true ? false : true
            }

            Rectangle {
                id: rectangle_quality_factor
                x: 688
                y: 68
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1
                TextInput {
                    id: textInput_q
                    text: backend.setData[5] == 0 ? "" : backend.setData[5]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
                visible: radioButton_l_section.checked == true ? false : true
            }

            ComboBox {
                id: comboBox_f_unit
                x: 825
                y: 16
                width: 97
                height: 30
                font.pointSize: 13
                model: ["Hz", "KHz", "MHz", "GHz"]
                currentIndex:
                {
                    if (backend.setData[8] == "Hz") return 0
                    if (backend.setData[8] == "KHz") return 1
                    if (backend.setData[8] == "MHz") return 2
                    if (backend.setData[8] == "GHz") return 3
                }
            }

            Text {
                id: text11
                x: 336
                y: 70
                text: qsTr("+")
                font.pixelSize: 22
            }

            Rectangle {
                id: rectangle_zl_im
                x: 354
                y: 69
                width: 70
                height: 30
                color: "#ffffff"
                border.width: 1
                TextInput {
                    id: textInput_zl_im
                    text: backend.setData[3] == 0 ? "" : backend.setData[3]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
            }

            Text {
                id: text12
                x: 429
                y: 18
                text: qsTr("j Ω")
                font.pixelSize: 22
            }

            Text {
                id: text14
                x: 336
                y: 18
                text: qsTr("+")
                font.pixelSize: 22
            }

            Rectangle {
                id: rectangle_zs_im
                x: 354
                y: 17
                width: 70
                height: 30
                color: "#ffffff"
                border.width: 1
                TextInput {
                    id: textInput_zs_im
                    text: backend.setData[1] == 0 ? "" : backend.setData[1]
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Arial"
                }
            }
        }

        Rectangle {
            id: rectangle_calculate
            x: 778
            y: 612
            width: 190
            height: 44
            color: "#ffffff"
            radius: 8

            Text {
                id: text4
                text: qsTr("Calculate")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 22
                anchors.horizontalCenter: parent.horizontalCenter
                font.bold: true
                font.family: "Arial"
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // Neu = "" thi dat la 0
                    backend.getParameter(textInput_zs_re.text == "" ? 0 : textInput_zs_re.text, textInput_zs_im.text == "" ? 0 : textInput_zs_im.text, textInput_zl_re.text == "" ? 0 : textInput_zl_re.text, textInput_zl_im.text == "" ? 0 : textInput_zl_im.text, textInput_f.text == "" ? 0 : textInput_f.text, textInput_q.text == "" ? 0 : textInput_q.text, comboBox_f_unit.currentText)
                    if (backend.checkFilled)
                    {
                        backend.calculate()
                        loader.source = "result.qml"
                    }
                    else
                    {
                        text_error.visible = true
                    }
                }
            }
        }

        Text {
            id: text_input_parameter
            x: 32
            y: 422
            text: qsTr("III. Input Parameter")
            font.pixelSize: 25
            font.family: "Arial"
        }

        Rectangle {
            id: rectangle_line
            x: 32
            y: 407
            width: 930
            height: 2
            color: "#000000"
        }

        Rectangle {
            id: rectangle_about
            x: 32
            y: 612
            width: 190
            height: 44
            color: "#ffffff"
            radius: 8
            Text {
                id: text13
                text: qsTr("About")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 22
                font.italic: true
                font.family: "Arial"
                font.bold: false
                anchors.horizontalCenter: parent.horizontalCenter
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    var component = Qt.createComponent("about.qml")
                    var window    = component.createObject(root)
                    window.show()
                }
            }
        }

        Text {
            id: text_error
            x: 262
            y: 623
            visible: false
            color: "#e03131"
            text: qsTr("Error! An error occurred, please check and try again\n")
            font.pixelSize: 19
            font.bold: true
            font.family: "Arial"
        }
    }
    // Connections {
    //     target: backend
    //     function onGetData(stringText)
    //     {
    //         header.text = stringText
    //     }
    // }


}
