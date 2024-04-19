import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: root
    width: 1000
    height: 680
    visible: true
    maximumHeight: 680
    maximumWidth: 1000
    minimumHeight: 680
    minimumWidth: 1000
    title: qsTr("Impedance Matching Network")
    
    property var calculated_result

    Loader {
        id: loader
        anchors.centerIn: parent
        width: 1000
        height: 680
        source: "calculator.qml"
    }
}
