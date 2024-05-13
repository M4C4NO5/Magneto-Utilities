function zoomIn() {
    var div = document.getElementById('vacancy-container');
    var width = div.offsetWidth;
    var height = div.offsetHeight;
    div.style.width = (width * 1.1) + 'px'; 
    div.style.height = (height * 1.1) + 'px';
  }
  
  function zoomOut() {
    var div = document.getElementById('vacancy-container');
    var width = div.offsetWidth;
    var height = div.offsetHeight;
    div.style.width = (width / 1.1) + 'px';
    div.style.height = (height / 1.1) + 'px';
  }
  
function progressIn(step){
    var div = document.getElementById('prBar');
    div.style.transition = 'width 0.5s ease-in-out';

    setTimeout(function() {

      switch (step){
        case 1: div.style.width = 33.33 + '%'; break;
        case 2: div.style.width = 66.66 + '%'; break;
        case 3: div.style.width = 100 + '%'; break;
        default: div.style.width = 0 + '%'; break;
      }
        
    }, 300); 
    
}




