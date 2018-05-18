//var TableArray = []
//    document.addEventListener('click', function ( e ) {
//    var element = document.getElementById(e.target.id)
//    if (element.classList.contains('tables')){
//        element.classList.remove('tables')
//        element.classList.add('tablesSelected')
//        TableArray.push(element.id)
//        var form = document.getElementById("reserve-form")
//        form.style.display="inline"
//        }
//    else if (element.classList.contains('tablesSelected')){
//        element.classList.remove('tablesSelected')
//        element.classList.add('tables')
//        var index = TableArray.indexOf(element.id)
//        if (index > -1){
//            TableArray.splice(index, 1)
//        }
//        if (TableArray.length == 0){
//        var form = document.getElementById("reserve-form")
//        form.style.display="none"
//        }
//    }
//});
//function sendData(){
//   var name =  document.getElementById('name').value
//   var email = document.getElementById('email').value
//   var date = document.getElementById('date').value
//   var data1 = new Object();
//   data1.name = name
//   data1.email = email
//   data1.date = '{{ date }}'
//   data1.tables = TableArray.join(",");
//   console.log(data1)
//    $.post(
//        url = "{{ url_for('index') }}",
//        data = data1
//    );
//   }
//function nextDay(){
//   var data1 = new Object();
//   data1.date = '{{ date }}'
//    $.post(
//        url = "{{ url_for('nextday') }}",
//        data = data1
//    );
//   }
//function previousDay(){
//   var data1 = new Object();
//   data1.date = '{{ date }}'
//    $.post(
//        url = "{{ url_for('previousday') }}",
//        data = data1
//    );
//   }
//function setTable(tableId, tableSizeW, tableSizeL, tableCoordW, tableCoordL, tableSeats, tableReserved, tableForm){
//    var newTable = document.createElement("div")
//    newTable.id = "table_"+tableId
//    if (tableReserved == '1'){
//        newTable.classList.add('tablesReserved')
//    }
//    else {
//    newTable.classList.add('tables');
//    }
//    newTable.style.width = 5*tableSizeW+"px"
//    newTable.style.height = 3*tableSizeL+"px"
//    newTable.style.border = "1px solid black"
//    newTable.style.position = "absolute"
//
//    newTable.innerHTML = tableSeats
//
//    if (tableForm == 'round'){
//        newTable.style.borderRadius = "50%"
//    }
//
//    strM = (tableCoordL*3-3*tableSizeL/2)+"px "+((100-tableCoordW)*5 - 5*tableSizeW)+"px "+(100-tableCoordL)*3+"px "+(tableCoordW*5 )+"px"
//
//    newTable.style.margin=strM
//    document.getElementById("hall").appendChild(newTable)
//    }