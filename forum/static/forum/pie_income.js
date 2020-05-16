function renderChart() //parameters should be data and labels
    var ctxP = document.getElementById("pieChart").getContext('2d');
    var myPieChart = new Chart(ctxP, {
      type: 'pie',
      data: {
        labels: ["Reed", "Green", "Yellow", "Grey", "Dark Grey"],
        datasets: [{
          data: [300, 50, 100, 40, 120],
          backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"],
          hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"]
        }]
      },
      options: {
        responsive: true
      }
    });

$("renderBtn").click(
    function(){
        data = [2000, 40000, 50000, 1500, 200]
        labels = ["Lawn Mowing", "Project A", "Project B", "Child Care", "Gain/Loss"]
        renderChart(data, labels)
    }
)