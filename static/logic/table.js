$.fn.switchColumns = function ( col1, col2 ) {
    var $this = this,
        $tr = $this.find('tr');

    $tr.each(function(i, ele){
        var $ele = $(ele),
            $td = $ele.find('td'),
            $th = $ele.find('th'),
            $tdt,
            $tht;
        
        // relocate th's
        $tht = $th.eq(col1).clone();
        $th.eq(col1)
        	.html( $th.eq(col2).html() )
        	.attr({
        		"class": $th.eq(col2).attr("class"),
        		"style": $th.eq(col2).attr("style")
    		});
        $th.eq(col2)
        	.html( $tht.html() )
        	.attr({
        		"class": $tht.attr("class"),
        		"style": $tht.attr("style")
        	});
        // relocate td's
        $tdt = $td.eq( col1 ).clone();
        $td.eq( col1 )
        	.html( $td.eq( col2 ).html() )
        	.attr("class", $td.eq( col2 ).attr("class"));
        $td.eq( col2 )
        	.html( $tdt.html() )
        	.attr("class", $tdt.attr("class"));
    });
};

$(window).load(function(){
	// Column hover action
	$("th").hover(function() {
		var colNo = $(this).index()
		$("table col").eq(colNo).addClass("colHover")
		$("table tbody tr").each(function(index) {
			$(this).find("td").eq(colNo).addClass("cellHover")
		});
	},function() {
		var colNo = $(this).index()
		$("table col").eq(colNo).removeClass("colHover")
		$("table tbody tr").each(function(index) {
			$(this).find("td").eq(colNo).removeClass("cellHover")
		});
	})
	
	// Column move action
	$('th').on('click', "button[class*='act-move-column-']", function() {
		var // find column situation
			columnLast = $("table col").length - 1,
			columnFirst = 0,
			columnCurrent = $(this).closest('th').index(),
			move = {to: undefined, from: undefined},
			// if this was a right/left action
			direction = $(this).attr("class").split("act-move-column-")[1].split(" ")[0]
		
		if (direction == 'left') {
			if (columnCurrent > columnFirst) {
				move.to = columnCurrent - 1
				move.from = columnCurrent
			} else if (columnCurrent == columnFirst) {
				console.log('No place to move to the LEFT!');
			}
		} else if (direction == 'right') {
			if (columnCurrent < columnLast) {
				move.to = columnCurrent + 1
				move.from = columnCurrent
			} else if (columnCurrent == columnLast) {
				console.log('No place to move to the RIGHT!');
			}
		}
		if (move.to != undefined && move.from != undefined) {
			$("table").switchColumns(move.from, move.to);
			$('th').eq(move.to).mouseleave();
		}
	});
});