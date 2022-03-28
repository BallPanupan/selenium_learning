window.console = window.console || function (t) {};

if (document.location.search.match(/type=embed/gi)) {
	window.parent.postMessage("resize", "*");
}

var rID = null;

var load = function (el, s, t) {
	var perc, k = 2;

	if (t % k === 0) {
	  perc = t / k;
	  el.dataset.perc = perc + '%';
	  el.style.backgroundSize =
		s.replace(/0px/g, el.dataset.perc);

	  if (perc === 100) {
		cancelAnimationFrame(rID);
		rID = null;
		document.getElementById("completed").style.display = "block";
		return;
	  }
	}

	rID = requestAnimationFrame(
	  load.bind(this, el, s, ++t));

  };

function main(){
	document.querySelector('button').
	addEventListener('click', function () {
		document.getElementById("completed").style.display = "none";
	  var s;
  
	  if (!rID) {
		this.classList.toggle('loading');
		s = getComputedStyle(this).backgroundSize;
		if (this.classList.contains('loading'))
		  load(this, s, 0);
		else {
		  this.dataset.perc =
			this.style.backgroundSize = '';
		}
	  }
	}, false);
}

  //# sourceURL=pen.js