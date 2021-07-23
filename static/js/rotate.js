
$('#img-rotate').on('click', function(e) {
	$('#rimg').rotate(getNextAngle());
})

nextAngle = 0;
function getNextAngle() {
    nextAngle += 90;    
    if(nextAngle >= 360) {
        nextAngle = 0;
    }
    return nextAngle;
}
