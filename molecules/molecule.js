var canvas_ref;

function debuter() {
	var canvas = document.getElementById("canvas_jeu");
	if (canvas.getContext) {
		var ctx = canvas.getContext("2d");
		// Trace les lignes verticales
		for (i=0;i<=480;i=i+60) {
			ctx.beginPath();
			ctx.fillStyle = 'rgb(0, 0, 0)';
			ctx.moveTo(i,0);
			ctx.lineTo(i,480);
			ctx.closePath();
			ctx.stroke();
		}
		// Trace les lignes horizontales
		for (i=0;i<=480;i=i+60) {
				ctx.beginPath();
				ctx.fillStyle = 'rgb(0, 0, 0)';
				ctx.moveTo(0,i);
				ctx.lineTo(640,i);
				ctx.closePath();
				ctx.stroke();
			}
			// Trace le contour
			ctx.beginPath();
			ctx.fillStyle = 'rgb(0, 0, 0)';
			ctx.moveTo(0,0); 
			ctx.lineTo(640,0);
			ctx.lineTo(640,480); 
			ctx.lineTo(0,480);
			ctx.lineTo(0,0);
			ctx.closePath();
			ctx.stroke();
	}
}

function canvas_clic(evt) {
	var canvas = document.getElementById("canvas_jeu");
	if (canvas.getContext) {
		var ctx = canvas.getContext("2d");
		console.log("X:"+evt.offsetX+" - Y:"+evt.offsetY);
	}
}


function initialisation() {
	canvas_ref = document.getElementById("canvas_jeu");
	canvas_ref.addEventListener("click", function(evt) {canvas_clic(evt);} );
}