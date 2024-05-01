function zoomIn() {
    var div = document.getElementById('vacancy-container');
    var width = div.offsetWidth;
    var height = div.offsetHeight;
    div.style.width = (width * 1.1) + 'px'; // Aumenta el tamaño en un 10%
    div.style.height = (height * 1.1) + 'px';
  }
  
  function zoomOut() {
    var div = document.getElementById('vacancy-container');
    var width = div.offsetWidth;
    var height = div.offsetHeight;
    div.style.width = (width / 1.1) + 'px'; // Reduce el tamaño en un 10%
    div.style.height = (height / 1.1) + 'px';
  }
  
  function progressIn(step){
    var div = document.getElementById('progress');
    var width = div.offsetWidth;
  
    
    

    
  }
  function progressOut(){
    var div = document.getElementById('progress');
    var width = div.offsetWidth;
   
  }