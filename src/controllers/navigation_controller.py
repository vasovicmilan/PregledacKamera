class NavigationController:
    def __init__(self, ui, camera_controller=None):
        self.ui = ui
        self.camera_controller = camera_controller
        self.stacked_widget = ui.stackedWidget
        self._connect_menu()

    def show_add_camera(self):
        if self.camera_controller:
            self.camera_controller.reset_add_form()
        self.stacked_widget.setCurrentWidget(self.ui.addCamera)

    # 🔗 MENU NAVIGATION
    def _connect_menu(self):
        self.ui.actionAllCameras.triggered.connect(self.show_camera_list)
        self.ui.actionAddCamera.triggered.connect(self.show_add_camera)
        self.ui.actionAbout.triggered.connect(self.show_about)

    # 📄 PAGES
    def show_camera_list(self):
        self.stacked_widget.setCurrentWidget(self.ui.cameraList)

    def show_about(self):
        self.stacked_widget.setCurrentWidget(self.ui.about)