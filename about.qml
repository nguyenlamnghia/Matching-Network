import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow  {
// Window {
    id: about
    width: 700
    height: 300
    title: "About"
    visible: true

    Rectangle {
        id: rectangle
        color: "#e9ecef"
        anchors.fill: parent
        Rectangle {
        id: rectangle1
        color: "#dee2e6"
        radius: 8
        border.color: "#ffffff"
        border.width: 2
        anchors.fill: parent
        anchors.leftMargin: 10
        anchors.rightMargin: 10
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        Text {
        id: text1
        text: qsTr("🖥️ Matching Network Calculator")
        anchors.verticalCenter: parent.verticalCenter
        font.pixelSize: 40
        anchors.verticalCenterOffset: -103
        anchors.horizontalCenterOffset: 0
        font.family: "Tahoma"
        font.bold: false
        anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: text2
            x: 35
            y: 100
            text: "Họ và tên: Nguyễn Lâm Nghĩa"
            font.pixelSize: 20
        }

        Text {
            id: text3
            x: 35
            y: 130
            text: "MSSV: 20214022"
            font.pixelSize: 20
        }

        Text {
            id: text4
            x: 35
            y: 159
            text: "Mã học phần: ET3241"
            font.pixelSize: 20
        }

        Text {
            id: text5
            x: 35
            y: 189
            text: "Mã lớp: 150111"
            font.pixelSize: 20
        }

        Text {
            id: text6
            x: 35
            y: 219
            text: "GVHD: Nguyễn Nam Phong"
            font.pixelSize: 20
        }

        Image {
            id: image
            x: 483
            y: 91
            width: 115
            height: 160
            source: "image/Hust_Logo.png"
            fillMode: Image.PreserveAspectFit
        }

        Rectangle {
            id: rectangle2
            x: 22
            y: 66
            width: 635
            height: 2
            color: "#000000"
        }
        }
    }
}
