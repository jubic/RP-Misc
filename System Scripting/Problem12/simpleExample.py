from graphy.backends import google_chart_api
#
chart = google_chart_api.BarChart()
chart.AddBars([60], label="Male")
chart.AddBars([40], label="Female")
chart.left.min = 0
chart.left.max = 100
chart.bottom.labels = ["Male", "Female"]
chart.bottom.label_positions = [25, 75]
chart.left.labels = range(0, 110, 10)
chart.left.label_gridlines = True
#
print chart.display.Img(300, 225)