import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QComboBox, QTableWidget
from PySide6.QtCore import Qt
from ui_form import Ui_Main

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.Table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.FAdd.clicked.connect(self.save_data)
        self.ui.NavEdit.clicked.connect(self.on_edit)
        self.ui.NavSave.clicked.connect(self.save_change)
        self.ui.NavDelete.clicked.connect(self.delete_row)
        self.ui.NavSave.setEnabled(False)

    def disable_rows(self):
        for row in range(self.ui.Table.rowCount()):
            for col in range(self.ui.Table.columnCount()):
                item = self.ui.Table.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def enable_row(self, row):
        for col in range(self.ui.Table.columnCount()):
            item = self.ui.Table.item(row, col)
            if item:
                item.setFlags(item.flags() | Qt.ItemIsEditable)

    def remove_combo(self, row):
        self.ui.Table.removeCellWidget(row, 1)

    def on_edit(self):
        selected_index = self.ui.Table.selectionModel().selection().indexes()

        if selected_index:
            row = selected_index[0].row()

            self.disable_rows()  # Deshabilita toda la tabla

            self.ui.NavEdit.setEnabled(False)
            self.ui.NavSave.setEnabled(True)

            self.enable_row(row)  # Habilita solo la fila seleccionada para edición

            # Crea el QComboBox y lo coloca en la celda correspondiente
            formOptions = QComboBox()
            formOptions.addItems([self.ui.FOptions.itemText(i) for i in range(self.ui.FOptions.count())])
            self.ui.Table.setCellWidget(row, 1, formOptions)

            self.ui.Table.setEditTriggers(QTableWidget.AllEditTriggers)  # Permite editar la tabla

    def save_change(self):
        selected_index = self.ui.Table.selectionModel().selection().indexes()

        if selected_index:
            row = selected_index[0].row()

            name_item = self.ui.Table.item(row, 0)
            if name_item:
                name_item.setText(name_item.text())

            # Obtén el texto del QComboBox y actualiza la celda correspondiente
            combo_widget = self.ui.Table.cellWidget(row, 1)
            if isinstance(combo_widget, QComboBox):
                combo_text = combo_widget.currentText()
                self.ui.Table.setItem(row, 1, QTableWidgetItem(combo_text))

            # Actualiza la descripción
            FDText = self.ui.Table.item(row, 2)
            if FDText:
                FDText.setText(FDText.text())

            # Elimina el QComboBox después de guardar
            self.remove_combo(row)

            self.disable_rows()  # Deshabilita todas las filas nuevamente
            self.ui.NavEdit.setEnabled(True)
            self.ui.NavSave.setEnabled(False)

    def save_data(self):
        data = {
            "name": self.ui.FNLable.text(),
            "priority": self.ui.FOptions.currentText(),
            "description": self.ui.FDText.toPlainText()
        }

        print(f"Datos guardados en memoria: {data}")

        row = self.ui.Table.rowCount()
        self.ui.Table.insertRow(row)
        self.ui.Table.setItem(row, 0, QTableWidgetItem(data["name"]))
        self.ui.Table.setItem(row, 1, QTableWidgetItem(data["priority"]))
        self.ui.Table.setItem(row, 2, QTableWidgetItem(data["description"]))

    def delete_row(self):
        selected_index = self.ui.Table.selectionModel().selection().indexes()

        if selected_index:
            row = selected_index[0].row()
            self.ui.Table.removeRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
