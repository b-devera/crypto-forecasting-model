
//REad json
const labelDate = [];
const predictP= [];
const actualP = [];

function drawGraph(){
    function getData(chart){
        fetch("../static/data/BTC-USD_Price_Prediction.json")
        .then(response => response.json())
        .then((json) => {
            //console.log(json.data.length);
            for (var i = 0;i < json.data.length; i++){
                labelDate.push(json.data[i].date);
                predictP.push(json.data[i].prediction);
                actualP.push(json.data[i].validation);
            };
            chart.update();
        })
        
    };
    
    //Create chart
    function drawPriceChart(){
        const data = {
            labels:labelDate,
            datasets: [
                {
                    data: predictP,
                    label: 'Predicted Prices',
                    fill: false,
                    borderColor: "#8e5ea2",
                    pointHoverBorderColor:"red",
                    pointHoverBackgroundColor:"red",
                    pointHoverRadius: 10
                },
                {
                    data: actualP,
                    label: 'Actual Prices',
                    fill: false,
                    borderColor: "#3e95cd",
                    hoverBorderColor: "blue",
                    pointHoverBorderColor:"blue",
                    pointHoverBackgroundColor:"blue",
                    pointHoverRadius: 10
                },
            ],
        };
        
        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                tooltips: {
                    mode: 'nearest',
                    intersect: false,
                },
                hover: {
                    mode: 'index',
                    intersect: false,
                },
                interaction: {
                    mode: 'x',
                    intersect: false
                },
                scales: {
                    y: {
                        ticks:{
                            callback: function  (value){
                                return '$' + value
                            },
                        },
                    },
                }, 
            },
            plugins: [{
                afterDraw: chart => {
                    if (chart.tooltip?._active?.length) {
                        let x = chart.tooltip._active[0].element.x;
                        let yAxis = chart.scales.y;
                        let ctx = chart.ctx;
                        ctx.save();
                        ctx.beginPath();
                        ctx.moveTo(x, yAxis.top);
                        ctx.lineTo(x, yAxis.bottom);
                        ctx.lineWidth = 1;
                        ctx.strokeStyle = '#000000';
                        ctx.stroke();
                        ctx.restore();
                    }
                }
            }],
        };
        
        const ctx = document.getElementById("myChart").getContext("2d");
        const myChart= new Chart(ctx, config);
        
        getData(myChart);
    }
    
    drawPriceChart();
}
drawGraph();


//Drawr pie chart
const dataSetSen = [];

function getDataSentimental(chart){

    fetch("../static/data/BTC_sentimental.json")
    .then(response => response.json())
    .then((json) => {
        //console.log(json.data.length);
        for (var i = 0;i < json.length; i++){
            if (json[i].date == "2022-11-30") {
                dataSetSen.push(json[i].total_negative);
                dataSetSen.push(json[i].total_neutral);
                dataSetSen.push(json[i].total_positive);
            }
        };
        chart.update();
    })
    
};

function drawTweetSentimental(){
    const ctx1 = document.getElementById("senChart").getContext("2d");
    const senData = {
        labels: [
            'Negative',
            'Neutral',
            'Positive'
        ],
        datasets: [{
            label: 'My First Dataset',
            data: dataSetSen,
            backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(207, 203, 203)'
            ],
            hoverOffset: 4
        }]
        };
    const config1 = {
        type: 'doughnut',
        data: senData,
        };
    const senChart= new Chart(ctx1, config1);
    getDataSentimental(senChart);
}
drawTweetSentimental();

//draw historical sentimental analysis
function drawHistoricalSentimental (){

    const labelsDate = [];
    const hisNeg = [];
    const hisPos = [];
    const hisNeu = [];

    function getData(chart){

        fetch("../static/data/BTC_sentimental.json")
        .then(response => response.json())
        .then((json) => {
            //console.log(json.data.length);
            for (var i = 0;i < json.length; i++){
                labelsDate.push(json[i].date);
                hisNeg.push(json[i].total_negative);
                hisPos.push(json[i].total_neutral);
                hisNeu.push(json[i].total_positive);
            };
            chart.update();
        })
    };
    

    const data = {
        labels: labelsDate,
        datasets: [
            {
                data: hisNeg,
                label: 'Negative',
                backgroundColor: 'rgb(255, 99, 132)',
            },
            {
                data: hisNeu,
                label: 'Neutral',
                backgroundColor: 'rgb(54, 162, 235)',
            },
            {
                data: hisPos,
                label: 'Positive',
                backgroundColor: 'rgb(207, 203, 203)',
            },
        ]
    };

    const ctx2 = document.getElementById("senChart2").getContext("2d");
    const config2 = {
        type: 'bar',
        data: data,
        options: {
            interaction: {
                mode: 'x'
            },
          scales: {
            y: {
              beginAtZero: true,
            },
            x: {
                stacked: true,
            }
          }
        },
      };
    const senChart2= new Chart(ctx2, config2);
    getData(senChart2);
            

}
drawHistoricalSentimental()
