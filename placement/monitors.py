from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.monitors.mixins import StatsMonitorMixin
# @monitors.name('Item count')
# class ItemCountMonitor(Monitor):

#     @monitors.name('Minimum number of items')
#     def test_minimum_number_of_items(self):
#         item_extracted = getattr(
#             self.data.stats, 'item_scraped_count', 0)
#         minimum_threshold = 10

#         msg = 'Extracted less than {} items'.format(
#             minimum_threshold)
#         self.assertTrue(
#             item_extracted >= minimum_threshold, msg=msg
#         )

@monitors.name('Item validation')
class ItemValidationMonitor(Monitor, StatsMonitorMixin):
# class ItemValidationMonitor(Monitor):

    @monitors.name('No item validation errors')
    def test_no_item_validation_errors(self):
        validation_errors = getattr(
            self.stats, 'spidermon/validation/fields/errors', 0
        )
        self.assertEqual(
            validation_errors,
            0,
            msg='Found validation errors in {} fields'.format(
                validation_errors)
        )

class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [
        # ItemCountMonitor,
        ItemValidationMonitor,
    ]
