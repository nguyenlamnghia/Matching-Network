import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 1000
    height: 680
    visible: true

    property var input_data: backend.setData
    property var calculated_result : backend.calculate

    Rectangle {
        id: rectangle
        color: "#e9ecef"
        anchors.fill: parent

        Rectangle {
            id: rectangle1
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
                id: text1
                text: "Impedance matching results"
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 40
                font.bold: false
                font.family: "Tahoma"
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        Rectangle {
            id: rectangle10
            x: 32
            y: 612
            width: 190
            height: 44
            color: "#ffffff"
            radius: 8
            Text {
                id: text13
                text: qsTr("👈  Back")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 22
                font.italic: false
                font.family: "Arial"
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    loader.source = "calculator.qml"
                }
            }
        }
        Rectangle {
            id: rectangle2
            x: 33
            y: 115
            width: 936
            height: 294
            color: "#ffffff"
            border.width: 1

            Text {
                id: text2
                y: 14
                text: qsTr("Question")
                font.pixelSize: 28
                horizontalAlignment: Text.AlignHCenter
                anchors.horizontalCenterOffset: 0
                font.italic: true
                font.underline: false
                font.bold: true
                font.family: "Arial"
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Image {
                id: image
                x: 32
                y: 69
                width: 259
                height: 181
                source: "image/" + calculated_result[3] + ".jpg"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: text3
                x: 118
                y: 254
                text: input_data[6]
                font.pixelSize: 20
                font.bold: false
                font.family: "Arial"
                font.underline: true
            }

            Rectangle {
                id: rectangle4
                x: 318
                y: 56
                width: 1
                height: 238
                color: "#000000"
            }

            Rectangle {
                id: rectangle5
                x: 0
                y: 56
                width: 936
                height: 1
                color: "#000000"
            }

            Text {
                id: text4
                x: 358
                y: 97
                text: qsTr("🔹 ") + input_data[7]
                font.pixelSize: 20
                font.bold: true
                font.family: "Arial"
            }

            Text {
                id: text5
                x: 358
                y: 133
                text: qsTr("🔹 Source Resistance (Zs): ") + (input_data[1] == 0 ? input_data[0] + qsTr(" Ω") : + input_data[0] + qsTr(" + ") + input_data[1] + qsTr("j Ω"))
                font.pixelSize: 20
                font.family: "Arial"
            }

            Text {
                id: text6
                x: 358
                y: 169
                text: qsTr("🔹 Load Resistance  (Zl): ") + (input_data[3] == 0 ? input_data[2] + qsTr(" Ω") : + input_data[2] + qsTr(" + ") + input_data[3] + qsTr("j Ω"))
                font.pixelSize: 20
                font.family: "Arial"
            }

            Text {
                id: text7
                x: 358
                y: 205
                text: qsTr("🔹 Frequence (f): ") + input_data[4] + qsTr(" ") + input_data[8]
                font.pixelSize: 20
                font.family: "Arial"
            }

            Text {
                id: text8
                x: 358
                y: 241
                text: qsTr("🔹 Quality factor (Q): ") + input_data[5]
                visible: input_data[6] != "L Section"
                font.pixelSize: 20
                font.family: "Arial"
            }
        }

        Rectangle {
            id: rectangle3
            x: 33
            y: 427
            width: 936
            height: 169
            color: "#d3f9d8"
            border.width: 1

            Text {
                id: text9
                y: 8
                text: qsTr("Result")
                font.pixelSize: 28
                font.family: "Arial"
                anchors.horizontalCenterOffset: 0
                anchors.horizontalCenter: parent.horizontalCenter
                font.italic: true
                font.bold: true
            }

            Rectangle {
                id: rectangle6
                x: 0
                y: 47
                width: 936
                height: 1
                color: "#000000"
            }

            Text {
                id: text10
                x: 66
                y: 75
                text: qsTr("🔹 Q value:")
                font.pixelSize: 20
                font.bold: true
                font.family: "Arial"
            }

            Text {
                id: text_q_result
                x: 190
                y: 75
                text: parseFloat(calculated_result[0]).toFixed(4)
                font.pixelSize: 20
                font.family: "Arial"
                font.bold: false
            }

            Text {
                id: text11
                x: 66
                y: 121
                text: qsTr("🔹 L value:")
                font.pixelSize: 20
                font.family: "Arial"
                font.bold: true
            }

            Text {
                id: text_l_result
                x: 190
                y: 121
                text: parseFloat(calculated_result[1]).toFixed(4) + qsTr(" nH")
                font.pixelSize: 20
                font.family: "Arial"
                font.bold: false
            }

            Text {
                id: text12
                x: 566
                y: 121
                text: qsTr("🔹 C value:")
                font.pixelSize: 20
                font.family: "Arial"
                font.bold: true
            }

            Text {
                id: text_c_result
                x: 690
                y: 121
                text: parseFloat(calculated_result[2]).toFixed(4) + qsTr(" pF")
                font.pixelSize: 20
                font.family: "Arial"
                font.bold: false
            }
        }
    }

}
