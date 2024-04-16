import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: root
    width: 1000
    height: 680
    visible: true
    title: qsTr("Impedance Matching Network")

    Loader {
        id: loader
        anchors.centerIn: parent
        width: 1000
        height: 680
        source: "calculator.qml"
    }
}
