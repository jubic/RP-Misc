from graphy.backends import google_chart_api
#
chart = google_chart_api.BarChart()
chart.AddBars([60,40], label="SEG")
chart.AddBars([30,70], label="SIT")
chart.left.min = 0
chart.left.max = 100
chart.bottom.labels = ["Male", "Male", "Female", "Female"]
chart.bottom.label_positions = [13, 38, 63, 88]
chart.left.labels = range(0, 110, 10)
chart.left.label_gridlines = True
#
print chart.display.Img(600, 450)