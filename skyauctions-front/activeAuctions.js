//https://www.taniarascia.com/javascript-mvc-todo-app/ as base
class ActiveAuctionModel {
    constructor() {
        this.auctions = [];
        this.filters = ["Any", "Any", "Any", ""];
    }

    bindAuctionListChanged(callback) {
        this.onAuctionsUpdate = callback;
      }

    loadAuctions(page=1, bin="", tier="", type="", itemName=""){
        var connectString = "http://skyauctionsapi.azurewebsites.net/api/auction/?activeOnly=true&page="+page;
        if (bin === ""){
            bin = "Any";
        } else if (bin === "Yes"){
            bin = "True";
        } else if (bin === "No"){
            bin = "False";
        }
        if (tier === ""){
            tier = "Any";
        }
        if (type === ""){
            type = "Any";
        }
        if (bin !== "" && bin !== "Any"){
            connectString += "&binOnly=" + bin; 
        }
        if (tier !== "" && tier !== "Any"){
            connectString += "&itemTier=" + tier; 
        }
        if (type !== "" && type !== "Any"){
            connectString += "&itemType=" + type;
        }
        if (itemName !== ""){
            connectString += "&itemName=" + itemName;
        }
    
        this.filters = [bin, tier, type, itemName];
        fetch(connectString)
        .then(response => response.json())
        .then(function(data){ 
            this.auctions = [];
            for (var i = 0; i < data.results.length; i++)
            {
                this.auctions.push(data.results[i]);
            }
            this.onAuctionsUpdate(this.auctions, page, parseInt(data.count/100)+1, this.filters); // i know this is divided by 100 because i paginated by 100 !MAGIC NUMBER
        }.bind(this))
        .catch(error => console.log(error));
    }
  }
  
  class ActiveAuctionView {
    constructor() {
        // The root element
        this.app = getElement('#root')

        // The title of the app
        this.title = createElement('h1', 'title')
        this.title.textContent = 'Active Auctions'

        // pages
        this.paginationNav = createElement('nav');
        this.pagination = createElement('ul', 'pagination');
        this.paginationNav.append(this.pagination);
        
        //expand all
        const expandAll = createElement('button');
        expandAll.setAttribute("type", "button")
        expandAll.classList.add("btn")
        expandAll.style.backgroundColor = "#DCDCDC"
        expandAll.setAttribute("data-bs-toggle", "collapse")
        expandAll.setAttribute("data-bs-target", ".multi-collapse")
        expandAll.ariaExpanded = false;
        expandAll.setAttribute("aria-controls","multi-collapse");
        expandAll.textContent = "Expand All"
        expandAll.style.marginBottom = "5px";
        expandAll.style.marginTop = "5px";

        //create filters
        this.filterDiv = createElement('form', 'row');
        //bin dropdown
        const binOptions = ["Any", "Yes", "No"];
        this.filterBin = createDropDown("binSelect", "BIN:", binOptions);
        this.filterDiv.append(this.filterBin)
        //tier dropdown
        const tierOptions = ["Any", "Common","Uncommon","Rare","Epic","Legendary", "Mythic", "Divine", "Special", "Very Special" ];
        this.filterTier = createDropDown("tierSelect", "Tier:", tierOptions);
        this.filterDiv.append(this.filterTier)
        // type dropdown
        const typeOptions = ["Any", "Weapon", "Armor", "Accessories", "Consumables", "Blocks", "Misc"]
        this.filterType = createDropDown("typeSelect", "Type:", typeOptions);
        this.filterDiv.append(this.filterType);
        // query item name
        const queryDiv = createElement("div", "col-auto")
        const queryLabel = createElement("label", "col-form-label");
        queryLabel.textContent = "Item Name: "
        this.queryInput = createElement("input", "form-control");
        this.queryInput.setAttribute("type", "text");
        queryDiv.append(queryLabel, this.queryInput);
        this.filterDiv.append(queryDiv);

        this.queryBtn = createElement("button", "btn");
        this.queryBtn.classList.add("btn-primary");
        const queryBtnDiv = createElement("div", "col-auto");
        queryBtnDiv.classList.add("mt-auto");
        this.queryBtn.textContent = "Search";
        queryBtnDiv.append(this.queryBtn);
        this.filterDiv.append(queryBtnDiv);

        // The visual representation of the auction list
        this.auctionList = createElement('div', 'row');
        this.auctionList.append(createElement('div', 'auction-list'));

        // wrap everything in content
        this.content = createElement('div', 'container')

        // Append the title, pagination, and auction list to the app
        this.content.append(this.title, this.paginationNav, this.filterDiv, expandAll, this.auctionList);
        this.app.append(this.content);
    }

    displayPages(curPage, totalPages){
        // Delete all nodes
        while (this.pagination.firstChild) {
            this.pagination.removeChild(this.pagination.firstChild)
        }
        const prev = createElement('li', 'page-item');
        prev.innerHTML = "<a class='page-link'>Previous</a>";
        const next = createElement('li', 'page-item');
        next.innerHTML = "<a class='page-link'>Next</a>";
        const p1 = createElement('li', 'page-item');
        p1.id = "activePage";
        p1.classList.add("active");
        p1.innerHTML = "<a class='page-link'>"+ curPage +"</a>";
        this.pagination.append(prev, p1)
        // if on page one, can't go to previous so disable
        if (curPage == 1)
        {
            prev.classList.add("disabled");
        }
        if (totalPages >= 2 && curPage != totalPages)
        {
            const p2 = createElement('li', 'page-item');
            p2.innerHTML = "<a class='page-link'>" + String(parseInt(curPage) + 1) +"</a>";
            this.pagination.append(p2);
            if (totalPages > 2)
            {
                const pdots = createElement('li', 'page-item');
                pdots.classList.add("disabled");
                pdots.innerHTML = "<a class='page-link'>...</a>";
                const paginationTotal = createElement('li', 'page-item');
                paginationTotal.innerHTML = "<a class='page-link'>" + totalPages +"</a>";    
                this.pagination.append(pdots, paginationTotal);    
            }
        }
        if (curPage == totalPages)
        {
            next.classList.add("disabled");
        }
        this.pagination.append(next);
    }

    displayAuctions(auctions){
        // Delete all nodes
        while (this.auctionList.firstChild) {
            this.auctionList.removeChild(this.auctionList.firstChild)
        }
        
        // Show default message
        if (auctions.length === 0) {
            const p = createElement('p')
            p.textContent = 'No Auctions Loaded'
            this.auctionList.append(p)
        } else {
            // Create todo item nodes for each todo in state
            auctions.forEach(auction => {
                this.auctionList.append(generateAuctionDisplay(auction));
            })            
        }
    }

    bindGoToPage(handler)
    {
        this.pagination.addEventListener('click', event =>{
            if (!event.target.classList.contains("disabled"))
            {
                var page = event.target.textContent;
                if (page == "Previous")
                {
                    page = parseInt($("#activePage")[0].textContent) - 1;
                }
                else if (page == "Next")
                {
                    page = parseInt($("#activePage")[0].textContent) + 1;
                }
                if (isNaN(page))
                {
                    page = 1
                }
                handler(page);
            }
        })
    }

    bindOnSearchClick(handler){
        this.queryBtn.addEventListener('click', event =>{
            event.preventDefault();
            handler(this.filterDiv)
        })
    }

    setFilters(filters){
        if (filters[0] === "True"){
            this.filterBin.children[1].value = "Yes";
        } else if (filters[0] == "False") {
            this.filterBin.children[1].value = "No";
        } else{
            this.filterBin.children[1].value = filters[0];
        }
        this.filterTier.children[1].value = filters[1];
        this.filterType.children[1].value = filters[2];
        this.queryInput.value = filters[3];
    }
  }
  
  class ActiveAuctionController {
    constructor(model, view) {
      this.model = model;
      this.view = view;

      //display auctions
      this.model.bindAuctionListChanged(this.onAuctionsUpdate);
      this.view.bindGoToPage(this.handleGoToPage);
      this.view.bindOnSearchClick(this.handleSearchClicked);
      this.onAuctionsUpdate(this.model.auctions, this.model.curPage, this.model.totalPages, this.model.filters);
    }

    onAuctionsUpdate = (auctions, curPage, totalPages, filters) => {
        this.view.setFilters(filters);
        this.view.displayAuctions(auctions);
        this.view.displayPages(curPage, totalPages);
    }

    handleGoToPage = page => {
        this.model.loadAuctions(page, this.model.filters[0], this.model.filters[1],this.model.filters[2],this.model.filters[3]);
    }

    handleSearchClicked = form => {
        var bin = form[0][form[0].selectedIndex].innerText;
        var tier = form[1][form[1].selectedIndex].innerText;
        var type= form[2][form[2].selectedIndex].innerText;
        var itemName = form[3].value;
        this.model.loadAuctions(1,bin, tier, type, itemName);
    }
  }
  
const app = new ActiveAuctionController(new ActiveAuctionModel(), new ActiveAuctionView());
app.model.loadAuctions()