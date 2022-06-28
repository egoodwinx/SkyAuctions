class NavigationModel {
    
}

class NavigationView {
    constructor() {
        // The root element
        this.nav = this.getElement('#navigation');
        const outerNav = this.createElement("nav", "navbar");
        outerNav.classList.add("navbar-expand-lg");
        outerNav.classList.add("bg-light");
        const navContainer = this.createElement("div", "container-fluid");
        const header = this.createElement("a", "navbar-brand");
        header.textContent = "SkyAuctions";
        header.href = "./index.html"

        const ul = this.createElement('ul', 'navbar-nav');
        ul.classList.add('me-auto');
        ul.classList.add('mb-2');
        ul.classList.add('mb-lg-0');
        const li = this.createElement('li', 'nav-item');
        const allAuctions = this.createElement('a', 'nav-link');
        allAuctions.href = "./allAuctions.html";
        allAuctions.textContent = "All Auctions";
        li.append(allAuctions);
        
        const liActiveAuctions = this.createElement('li', 'nav-item');
        const aActiveAuctions = this.createElement('a', 'nav-link');
        aActiveAuctions.href = "./activeAuctions.html";
        aActiveAuctions.textContent = "Active Auctions";
        liActiveAuctions.append(aActiveAuctions);

        const liStatistics = this.createElement('li', 'nav-item');
        const aStatistics = this.createElement('a', 'nav-link');
        aStatistics.href = "./itemStatistics.html";
        aStatistics.textContent = "Statistics";
        liStatistics.append(aStatistics);

        ul.append(li,liActiveAuctions, liStatistics);
        navContainer.append(header, ul);
        outerNav.append(navContainer);
        this.nav.append(outerNav);
    }

    // Create an element with an optional CSS class
    createElement(tag, className) {
        const element = document.createElement(tag);
        if (className) element.classList.add(className);

        return element;
    }

    // Retrieve an element from the DOM
    getElement(selector) {
        const element = document.querySelector(selector)

        return element
    }
}

class NavigationController {
    constructor(model, view) {
        this.model = model;
        this.view = view;
    }
  
}

const nav = new NavigationController(new NavigationModel(), new NavigationView())
