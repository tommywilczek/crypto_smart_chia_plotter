from os_service import OsService
from logger import Logger
from local_constants import OPERATING_SYSTEM, DRIVE_LIST, PLOT_MODE

logger = Logger()

def main():
    os_service = OsService(logger)

    logger.log("------ smart_plot has been started for " + OPERATING_SYSTEM + " machine ------")
    try:
        if(PLOT_MODE == "Add"):
            plot_pool_plots_until_drives_are_full(os_service)
        elif(PLOT_MODE == "Replace"):
            replace_og_plots_with_pool_plots(os_service)
        else:
            e = 'Incorrect OS in constants file.'
            logger.log("EXCEPTION: " + e)
            raise ValueError()
    except Exception as e:
        logger.log("EXCEPTION: " + str(e))
    logger.log("------  smart_plot has completed for " + OPERATING_SYSTEM + " machine   ------")

def plot_pool_plots_until_drives_are_full(os_service):
    while True:
        drive = os_service.find_drive_with_space(DRIVE_LIST)
        if drive == "":
            break
        os_service.plot_to_drive(drive + "Pool/")

def replace_og_plots_with_pool_plots(os_service):
    while True:
        drive = os_service.find_drive_with_og_plots(DRIVE_LIST)
        if drive == "":
            break
        os_service.replace_og_with_pool_plot(drive)

main()
