from os_service import OsService

class WindowsService(OsService):
    def find_drive_with_space(self, drive_list):
        return super().find_drive_with_space(drive_list)

    def drive_has_space(self, drive):
        return super().drive_has_space(drive)

    def count_files_in_dir(self, dir: str):
        return super().count_files_in_dir(dir)

    def get_available_space_on_drive_in_gb(self, drive: str):
        return super().get_available_space_on_drive_in_gb(drive)

    def plot_to_drive(self, drive: str):
        return super().plot_to_drive(drive)

    def clear_ssd(self):
        return super().clear_ssd()