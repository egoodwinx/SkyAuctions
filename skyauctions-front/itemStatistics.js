//https://www.taniarascia.com/javascript-mvc-todo-app/ as base
class StatisticsModel {
    constructor() {
        this.hourlyMaxData = [];
        this.hourlyMinData = [];
        this.hourlyAvgData = [];
        this.dailyMaxData = []; 
        this.dailyMinData = []; 
        this.dailyAvgData = []; 
        this.itemsIncluded=[];
    }

    bindStatisticsChanged(callback){
        this.onStatisticsUpdate = callback;
    }

    GetDailyItemAverages(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetDailyItemAverages?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            if (data.length > 0){
                data = data[0]
            }
            this.dailyAvgData = data;
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetDailyItemMins(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetDailyItemMins?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            if (data.length > 0){
                data = data[0]
            }
            this.dailyMinData = data;
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetDailyItemMaxes(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetDailyItemMaxes?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            if (data.length > 0){
                data = data[0]
            }
            this.dailyMaxData = data;
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetHourlyItemAverages(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetHourlyItemAverages?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            this.hourlyAvgData = [];
            var arrayPos = 0;
            for (var i = 0; i < 24; i++){ // 24 hours
                if (data.length > arrayPos){
                    if (data[arrayPos][0] === i){
                        this.hourlyAvgData.push(data[arrayPos][1]);
                        arrayPos++;
                    }
                    else{
                        this.hourlyAvgData.push(0);
                    }
                }
                else{
                    this.hourlyAvgData.push(0);
                }
            } 
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetHourlyItemMins(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetHourlyItemMins?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            this.hourlyMinData = [];
            var arrayPos = 0;
            for (var i = 0; i < 24; i++){ // 24 hours
                if (data.length > arrayPos){
                    if (data[arrayPos][0] === i){
                        this.hourlyMinData.push(data[arrayPos][1]);
                        arrayPos++;
                    }
                    else{
                        this.hourlyMinData.push(0);
                    }
                }
                else{
                    this.hourlyMinData.push(0);
                }
            } 
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetHourlyItemMaxes(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetHourlyItemMaxes?itemName="+itemQuery;
        
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            data = JSON.parse(data);
            this.hourlyMaxData = [];
            var arrayPos = 0;
            for (var i = 0; i < 24; i++){ // 24 hours
                if (data.length > arrayPos){
                    if (data[arrayPos][0] === i){
                        this.hourlyMaxData.push(data[arrayPos][1]);
                        arrayPos++;
                    }
                    else{
                        this.hourlyMaxData.push(0);
                    }
                }
                else{
                    this.hourlyMaxData.push(0);
                }
            } 
        }.bind(this))
        .catch(error => console.log(error));
    }

    GetItemNameResults(itemQuery){
        var connectString = "https://skyauctionsapi.azurewebsites.net/api/GetItemNameResults?itemName="+itemQuery;
        return fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            this.itemsIncluded = data;
        }.bind(this))
        .catch(error => console.log(error));
    }
  }
  
  class StatisticsView {
    constructor() {
        // The root element
        this.app = getElement('#root')

        // The title of the app
        this.title = createElement('h1', 'title')
        this.title.textContent = 'Statistics'
        // pages
        this.paginationNav = createElement('nav');
        this.pagination = createElement('ul', 'pagination');
        this.paginationNav.append(this.pagination);

        const searchDiv = createElement('div', 'row')
        const searchLabelCol = createElement('div', 'col-auto');
        const searchInputCol = createElement('div', 'col-auto');
        const searchButtonCol = createElement('div', 'col-auto');
        const searchLabel = createElement('label', 'form-label');
        searchLabel.textContent = "Search Item Name: ";
        searchLabelCol.append(searchLabel)
        this.searchBar = createElement('input', 'form-control');
        this.searchBar.setAttribute('type', 'text');
        searchInputCol.append(this.searchBar);
        this.searchButton = createElement('button', 'btn');
        this.searchButton.classList.add('btn-primary');
        this.searchButton.textContent = "Search";
        searchButtonCol.append(this.searchButton);
        const textInfo = createElement('div');
        textInfo.textContent = "* can use sql queries as input is not sanitized as per instructions";
        searchDiv.append(searchLabelCol, searchInputCol, searchButtonCol, textInfo);

        this.statisticsDiv = createElement('div');

        this.dailyChartDiv = createElement('div');
        this.dailyChartCanvas = createElement('canvas');
        this.dailyChartCanvas.id="dailyStatistics";
        this.dailyChartDiv.append(this.dailyChartCanvas);

        this.hourlyChartDiv = createElement('div');
        this.hourlyChartCanvas = createElement('canvas');
        this.hourlyChartCanvas.id = "hourlyStatistics";
        this.hourlyChartDiv.append(this.hourlyChartCanvas);

        this.statisticsDiv.append(this.dailyChartDiv, this.hourlyChartDiv);

        this.itemsQueriedDiv =  createElement('div');
        const itemsQueriedLabel = createElement('label');
        itemsQueriedLabel.textContent = "Showing results for the following items:"
        this.itemsQueriedList = createElement('div');
        this.itemsQueriedDiv.append(itemsQueriedLabel,this.itemsQueriedList);
        // wrap everything in content
        this.content = createElement('div', 'container');

        // Append the title, pagination, and auction list to the app
        this.content.append(this.title, this.paginationNav, searchDiv, this.itemsQueriedDiv, this.statisticsDiv);
        this.app.append(this.content);
    }

    bindOnSearchClick(handler){
        this.searchButton.addEventListener('click', event =>{
            event.preventDefault();
            var search = "";
            if (this.searchBar.value){
                search = this.searchBar.value.replace("'", "''");
            }
            handler(search);
        })
    }

    displayStatistics(dailyMaxes, dailyMins, dailyAvgs, hourlyMaxes, hourlyMins, hourlyAvgs, itemsQueried){
        this.displayItemsQueried(itemsQueried);
        const weekdayLabels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
        const weekdayData = {
            labels:weekdayLabels,
            datasets:[{
                label:"Maxes",
                data: dailyMaxes,
                borderColor: "FireBrick"
            },
            {
                label:"Averages",
                data: dailyAvgs,
                borderColor: "BurlyWood"           
            },
            {
                label:"Mins",
                data: dailyMins,
                borderColor: "CornflowerBlue"
            }]
        }
        const weekdayConfig = {
            type: 'line',
            data: weekdayData,
            options: {}
          };
        if (this.weekdayChart){
            this.weekdayChart.destroy();
        }
        this.weekdayChart = new Chart(document.getElementById('dailyStatistics'), weekdayConfig);

        const hourlyLabels = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"];
        const hourlyData = {
            labels:hourlyLabels,
            datasets:[{
                label:"Maxes",
                data: hourlyMaxes,
                borderColor: "FireBrick"
            },
            {
                label:"Averages",
                data:hourlyAvgs,
                borderColor: "BurlyWood"       
            },
            {
                label:"Mins",
                data:hourlyMins,
                borderColor: "CornflowerBlue"
            }]
        }
        const hourlyConfig = {
            type: 'line',
            data: hourlyData,
            options: {}
          };
        if (this.hourlyChart){
            this.hourlyChart.destroy();
        }
        this.hourlyChart = new Chart(document.getElementById('hourlyStatistics'), hourlyConfig);
    }

    displayItemsQueried(items){
        this.itemsQueriedList.textContent = items;
    }
  }
  
  class StatisticsController {
    constructor(model, view) {
      this.model = model;
      this.view = view;
      this.handleSearchClicked = this.handleSearchClicked.bind(this);
      this.model.bindStatisticsChanged(this.onStatisticsUpdate)
      this.view.bindOnSearchClick(this.handleSearchClicked);
      this.view.displayStatistics([],[],[],[],[],[],[]);
    }

    onStatisticsUpdate = () =>{
        this.view.displayStatistics(dailyMaxes, dailyMins, dailyAvgs, hourlyMaxes, hourlyMins, hourlyAvgs, itemsQueried);
    }

    async handleSearchClicked (itemName) {
        Promise.all([
            this.model.GetItemNameResults(itemName),
            this.model.GetDailyItemAverages(itemName),
            this.model.GetDailyItemMaxes(itemName),
            this.model.GetDailyItemMins(itemName),
            this.model.GetHourlyItemAverages(itemName),
            this.model.GetHourlyItemMaxes(itemName),
            this.model.GetHourlyItemMins(itemName)            
        ]).then(data => this.onStatisticsUpdate(this.model.dailyMaxData, this.model.dailyMinData, this.model.dailyAvgData,
            this.model.hourlyMaxData, this.model.hourlyMinData, this.model.hourlyAvgData, this.model.itemsIncluded));
    }

    // handleSearchClicked(){
    //     this.callGetters().then(this.onStatisticsUpdate(this.model.dailyMaxData, this.model.dailyMinData, this.model.dailyAvgData,
    //         this.model.hourlyMaxData, this.model.hourlyMinData, this.model.hourlyAvgData, this.model.itemsIncluded))
    // }
  }
  
  const app = new StatisticsController(new StatisticsModel(), new StatisticsView());