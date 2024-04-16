import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 1000
    height: 680
    visible: true
    title: qsTr("Hello World")

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
                text: qsTr("🖥️ Matching Network Calculator")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 40
                font.bold: false
                font.family: "Tahoma"
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        Rectangle {
            id: rectangle2
            x: 32
            y: 153
            width: 936
            height: 201
            color: "#ffffff"

            Image {
                id: image
                x: 16
                y: 8
                width: 239
                height: 147
                source: "image/L-Match.jpg"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image1
                x: 346
                y: 8
                width: 245
                height: 152
                source: "image/T-Match.jpg"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: image2
                x: 683
                y: 8
                width: 245
                height: 147
                source: "image/Pi-Match.jpg"
                fillMode: Image.PreserveAspectFit
            }

            RadioButton {
                id: radioButton2
                x: 72
                y: 152
                text: qsTr("L Section")
                font.pointSize: 15
            }

            RadioButton {
                id: radioButton3
                x: 404
                y: 152
                text: qsTr("T Section")
                font.pointSize: 15
            }

            RadioButton {
                id: radioButton4
                x: 738
                y: 152
                text: qsTr("PI Section")
                font.pointSize: 15
            }
        }

        Text {
            id: text2
            x: 32
            y: 113
            text: qsTr("I. Choose type of impedance matching network")
            font.pixelSize: 25
            font.family: "Arial"
        }

        Text {
            id: text3
            x: 32
            y: 363
            text: qsTr("II. Select circuit type")
            font.pixelSize: 25
            font.family: "Arial"
        }

        RadioButton {
            id: radioButton
            x: 384
            y: 359
            text: qsTr("DC feed")
            font.pointSize: 15
        }

        RadioButton {
            id: radioButton1
            x: 644
            y: 360
            text: qsTr("DC Block")
            font.pointSize: 15
        }

        Rectangle {
            id: rectangle3
            x: 32
            y: 474
            width: 936
            height: 114
            color: "#ffffff"

            Text {
                id: text6
                x: 21
                y: 18
                text: qsTr("Input impedance (Zin)")
                font.pixelSize: 22
            }

            Rectangle {
                id: rectangle6
                x: 250
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1
                anchors.verticalCenter: text6.verticalCenter
                anchors.verticalCenterOffset: 0

                TextInput {
                    id: textInput
                    text: qsTr("0")
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                }
            }

            Text {
                id: text7
                x: 384
                y: 18
                text: qsTr("Ω")
                font.pixelSize: 22
            }

            Text {
                id: text8
                x: 21
                y: 70
                text: qsTr("Load impedance (Zl)")
                font.pixelSize: 22
            }

            Rectangle {
                id: rectangle7
                x: 250
                y: 69
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1

                TextInput {
                    id: textInput1
                    text: qsTr("0")
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                }
            }

            Text {
                id: text9
                x: 384
                y: 70
                text: qsTr("Ω")
                font.pixelSize: 22
            }

            Text {
                id: text10
                x: 495
                y: 18
                text: qsTr("Frequency (f)")
                font.pixelSize: 22
            }
            Rectangle {
                id: rectangle8
                x: 688
                y: 16
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1

                TextInput {
                    id: textInput2
                    text: qsTr("0")
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                }
            }

            Text {
                id: text11
                x: 827
                y: 18
                text: qsTr("Hz")
                font.pixelSize: 22
            }

            Text {
                id: text12
                x: 495
                y: 70
                text: qsTr("Quality Factor (Q)")
                font.pixelSize: 22
            }

            Rectangle {
                id: rectangle9
                x: 688
                y: 68
                width: 123
                height: 30
                color: "#ffffff"
                border.width: 1
                TextInput {
                    id: textInput3
                    text: qsTr("0")
                    anchors.fill: parent
                    anchors.leftMargin: 10
                    font.pixelSize: 19
                    verticalAlignment: Text.AlignVCenter
                }
            }
        }

        Rectangle {
            id: rectangle4
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
        }

        Text {
            id: text5
            x: 32
            y: 422
            text: qsTr("III. Input Parameter")
            font.pixelSize: 25
            font.family: "Arial"
        }

        Rectangle {
            id: rectangle5
            x: 32
            y: 407
            width: 930
            height: 2
            color: "#000000"
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
                text: qsTr("About")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 22
                font.italic: true
                font.family: "Arial"
                font.bold: false
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }


}
