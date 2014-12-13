function Pager1(tableName1, itemsPerPage1) {
    this.tableName1 = tableName1;
    this.itemsPerPage1 = itemsPerPage1;
    this.currentPage1 = 1;
    this.pages1 = 0;
    this.inited = false;
    
    this.showRecords1 = function(from, to) {        
        var rows = document.getElementById(tableName1).rows;
        // i starts from 1 to skip table header row
        for (var i = 1; i < rows.length; i++) {
            if (i < from || i > to)  
                rows[i].style.display = 'none';
            else
                rows[i].style.display = '';
        }
    }
    
    this.showPage1 = function(pageNumber1) {
    	if (! this.inited) {
    		alert("not inited");
    		return;
    	}

        var oldPageAnchor = document.getElementById('pg1'+this.currentPage1);
        oldPageAnchor.className = 'pg-normal1';
        
        this.currentPage1 = pageNumber1;
        var newPageAnchor = document.getElementById('pg1'+this.currentPage1);
        newPageAnchor.className = 'pg-selected1';
        
        var from = (pageNumber1 - 1) * itemsPerPage1 + 1;
        var to = from + itemsPerPage1 - 1;
        this.showRecords1(from, to);
    }   
    
    this.prev = function() {
        if (this.currentPage1 > 1)
            this.showPage1(this.currentPage1 - 1);
    }
    
    this.next = function() {
        if (this.currentPage1 < this.pages1) {
            this.showPage1(this.currentPage1 + 1);
        }
    }                        
    
    this.init = function() {
        var rows = document.getElementById(tableName1).rows;
        var records = (rows.length - 1); 
        this.pages1 = Math.ceil(records / itemsPerPage1);
        this.inited = true;
    }

    this.showPageNav1 = function(pagerName1, positionId) {
    	if (! this.inited) {
    		alert("not inited");
    		return;
    	}
    	var element = document.getElementById(positionId);
    	
    	var pagerHtml1 = '<span onclick="' + pagerName1 + '.prev();" class="pg-normal1"> << </span> ';
        for (var page1 = 1; page1 <= this.pages1; page1++) 
            pagerHtml1 += '<span id="pg1' + page1 + '" class="pg-normal1" onclick="' + pagerName1 + '.showPage1(' + page1 + ');">' + page1 + '</span> ';
        pagerHtml1 += '<span onclick="'+pagerName1+'.next();" class="pg-normal1"> >> </span>';            
        
        element.innerHTML = pagerHtml1;
    }
}

