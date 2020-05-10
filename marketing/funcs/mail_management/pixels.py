import pytracking


# open_tracking_url = pytracking.get_open_tracking_url(
#     {"customer_id": 1}, base_open_tracking_url="http://127.0.0.1:8000/open/",
#     webhook_url="http://up419.siz.co.il/up1/dnxinzmvjk5t.jpg", include_webhook_url=True)
# print(open_tracking_url)


#     # This will produce a URL such as:
#     # https://trackingdomain.com/path/e30203jhd9239754jh21387293jhf989sda=
#
#
#
configuration = pytracking.Configuration(
    base_open_tracking_url="http://www.sl-op.com/open/",
    webhook_url="http://up419.siz.co.il/up1/dnxinzmvjk5t.jpg",
    include_webhook_url=False)

open_tracking_url = pytracking.get_open_tracking_url(
    {"customer_id": 1}, configuration=configuration)

print(open_tracking_url)
#
#     This will produce a URL such as:
#     https://trackingdomain.com/path/e30203jhd9239754jh21387293jhf989sda=
#
#
#
# click_tracking_url = pytracking.get_click_tracking_url(
#     "http://www.example.com/?query=value", {"customer_id": 1},
#     base_click_tracking_url="https://trackingdomain.com/path/",
#     webhook_url="http://requestb.in/123", include_webhook_url=True)
#
#     # This will produce a URL such as:
#     # https://trackingdomain.com/path/e30203jhd9239754jh21387293jhf989sda=
#
#
#
# Get Open Tracking Data from URL

# full_url = "http://www.sapiryoga.com/open/eyJtZXRhZGF0YSI6IHsiY3VzdG9tZXJfaWQiOiAxfX0="
# tracking_result = pytracking.get_open_tracking_result(
#     full_url, base_open_tracking_url="http://127.0.0.1:8000/open/")
# print(tracking_result.metadata)

    # Metadata is in tracking_result.metadata
    # Webhook URL is in tracking_result.webhook_url
#
#
# # Get Click Tracking Data from URL
#
# full_url = "https://trackingdomain.com/path/e30203jhd9239754jh21387293jhf989sda="
# tracking_result = pytracking.get_open_tracking_result(
#     full_url, base_click_tracking_url="https://trackingdomain.com/path/")
#
# # Metadata is in tracking_result.metadata
# # Webhook URL is in tracking_result.webhook_url
# # Tracked URL to redirect to is in tracking_result.tracked_url


#Get a 1x1 transparent PNG pixel
#
# (pixel_byte_string, mime_type) = pytracking.get_open_tracking_pixel()
# print((pixel_byte_string, mime_type))

