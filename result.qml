import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 1000
    height: 680
    visible: true

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
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                loader.source = "calculator.qml"
            }
        }
    }


}
