function calculate(grades){
  var week = document.getElementById("weekselect").value || 0;

var attTotal = 0;
var hwTotal = 0;
var advTotal = 0;
var ecTotal = 0;

document.getElementById("week0").style.visibility="hidden";
document.getElementById("week0Alt").style.visibility="visible";
document.getElementById("week0Alt2").style.visibility="visible";
document.getElementById("week0Alt3").style.visibility="visible";

if(week >= 1){
document.getElementById("week1").style.visibility="visible";
//no attendance
hwTotal += parseFloat(document.getElementById("hw1").value || 0);
//no advHomework
ecTotal += parseFloat(document.getElementById("ec1").value || 0);
}
else document.getElementById("week1").style.visibility="hidden";
if(week >= 2){
document.getElementById("week2").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec2").value || 0);
attTotal += parseFloat(document.getElementById("att2").value || 0);
hwTotal += parseFloat(document.getElementById("hw2").value || 0);
var temp = parseFloat(document.getElementById("adv2").value || 0);
if(temp != 0)
	advTotal += 10;
}
else document.getElementById("week2").style.visibility="hidden";
if(week >= 3){
document.getElementById("week3").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec3").value || 0);
attTotal += parseFloat(document.getElementById("att3").value || 0);
hwTotal += parseFloat(document.getElementById("hw3").value || 0);
var temp = parseFloat(document.getElementById("adv3").value || 0);
if(temp != 0 && advTotal == 0)
	advTotal += 10;
else if(temp != 0)
  advTotal += 5;
}
else document.getElementById("week3").style.visibility="hidden";
if(week >= 4){
document.getElementById("week4").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec4").value || 0);
attTotal += parseFloat(document.getElementById("att4").value || 0);
hwTotal += parseFloat(document.getElementById("hw4").value || 0);
var temp = parseFloat(document.getElementById("adv4").value || 0);
if(temp != 0)
	advTotal += 10;
}
else document.getElementById("week4").style.visibility="hidden";
if(week >= 5){
document.getElementById("week5").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec5").value || 0);
attTotal += parseFloat(document.getElementById("att5").value || 0);
hwTotal += parseFloat(document.getElementById("hw5").value || 0);
var temp4 = parseFloat(document.getElementById("adv4").value || 0);
var temp5 = parseFloat(document.getElementById("adv5").value || 0);
if(temp4 == 0 && temp5 != 0)
	advTotal += 10;
else if(temp4 != 0 && temp5 != 0)
  advTotal += 5;
}
else document.getElementById("week5").style.visibility="hidden";
if(week >= 6){
document.getElementById("week6").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec6").value || 0);
attTotal += parseFloat(document.getElementById("att6").value || 0);
hwTotal += parseFloat(document.getElementById("hw6").value || 0);
var temp4 = parseFloat(document.getElementById("adv4").value || 0);
var temp5 = parseFloat(document.getElementById("adv5").value || 0);
var temp6 = parseFloat(document.getElementById("adv6").value || 0);
if(temp4 == 0 && temp5 == 0 && temp6 != 0)
	advTotal += 10;
else if((temp4 != 0 || temp5 != 0) && temp6 != 0 )
  advTotal += 5;
}
else document.getElementById("week6").style.visibility="hidden";
if(week >= 7){
document.getElementById("week7").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec7").value || 0);
attTotal += parseFloat(document.getElementById("att7").value || 0);
hwTotal += parseFloat(document.getElementById("hw7").value || 0);
var temp = parseFloat(document.getElementById("adv7").value || 0);
if(temp != 0)
	advTotal += 10;
}
else document.getElementById("week7").style.visibility="hidden";
if(week >= 8){
document.getElementById("week8").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec8").value || 0);
attTotal += parseFloat(document.getElementById("att8").value || 0);
//no homework week 8
//no advanced week 8
}
else document.getElementById("week8").style.visibility="hidden";
if(week >= 9){
document.getElementById("week9").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec9").value || 0);
//no attendance week 9
//no homework week 9
//no advanced homework week 9
}
else document.getElementById("week9").style.visibility="hidden";
if(week >= 10){
document.getElementById("week10").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec10").value || 0);
attTotal += parseFloat(document.getElementById("att10").value || 0);
hwTotal += parseFloat(document.getElementById("hw10").value || 0);
var temp7 = parseFloat(document.getElementById("adv7").value || 0);
var temp10 = parseFloat(document.getElementById("adv10").value || 0);
if(temp7 == 0 && temp10 != 0)
	advTotal += 10;
else if(temp7 != 0 && temp10 != 0 )
  advTotal += 5;
}
else document.getElementById("week10").style.visibility="hidden";
if(week >= 11){
document.getElementById("week11").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec11").value || 0);
attTotal += parseFloat(document.getElementById("att11").value || 0);
hwTotal += parseFloat(document.getElementById("hw11").value || 0);
var temp7 = parseFloat(document.getElementById("adv7").value || 0);
var temp10 = parseFloat(document.getElementById("adv10").value || 0);
var temp11 = parseFloat(document.getElementById("adv11").value || 0);
if(temp7 == 0 && temp10 == 0 && temp11 != 0)
	advTotal += 10;
else if((temp7 != 0 || temp10 != 0) && temp11 != 0 )
  advTotal += 5;
}
else document.getElementById("week11").style.visibility="hidden";
if(week >= 12){
document.getElementById("week12").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec12").value || 0);
attTotal += parseFloat(document.getElementById("att12").value || 0);
hwTotal += parseFloat(document.getElementById("hw12").value || 0);
var temp = parseFloat(document.getElementById("adv12").value || 0);
if(temp != 0 && advTotal < 30)
	advTotal += 10;
else if(temp != 0 && advTotal >= 30)
  advTotal += 5;
}
else document.getElementById("week12").style.visibility="hidden";
if(week >= 13){
document.getElementById("week13").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec13").value || 0);
var att = parseFloat(document.getElementById("att13").value || 0);
if(attTotal >= 30)
  attTotal += att/2;
else{
  while(att > 0 && attTotal < 30){
    attTotal++;
    att--;
  }
  attTotal += att;
}
var hw = parseFloat(document.getElementById("hw13").value || 0);
if(hwTotal >= 40)
  hwTotal += hw/2;
else{
	while(hw > 0 && hwTotal < 40){
    hwTotal++;
    hw--;
  }
  hwTotal += hw/2;
}
var temp12 = parseFloat(document.getElementById("adv12").value || 0);
var temp13 = parseFloat(document.getElementById("adv13").value || 0);
if(temp12 == 0 && temp13 != 0 && advTotal < 30)
	advTotal += 10;
else if(temp12 == 0 && temp13 != 0 && advTotal >= 30)
  advTotal += 5;
else if(temp12 != 0 && temp13 != 0)
  advTotal += 5;
}
else document.getElementById("week13").style.visibility="hidden";
if(week >= 14){
document.getElementById("week14").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec14").value || 0);
var att = parseFloat(document.getElementById("att14").value || 0);
if(attTotal >= 30)
  attTotal += att/2;
else{
  while(att > 0 && attTotal < 30){
    attTotal++;
    att--;
  }
  attTotal += att;
}
var hw = parseFloat(document.getElementById("hw14").value || 0);
if(hwTotal >= 40)
  hwTotal += hw/2;
else{
  while(hw > 0 && hwTotal < 40){
    hwTotal++;
    hw--;
  }
  hwTotal += hw/2;
}
var temp12 = parseFloat(document.getElementById("adv12").value || 0);
var temp13 = parseFloat(document.getElementById("adv13").value || 0);
var temp14 = parseFloat(document.getElementById("adv14").value || 0);
if(temp12 == 0 && temp13 == 0 && temp14 != 0 && advTotal < 30)
	advTotal += 10;
else if(temp12 == 0 && temp13 == 0 && temp14 != 0 && advTotal >= 30)
  advTotal += 5;
else if((temp12 != 0 || temp13 != 0) && temp14 != 0 )
  advTotal += 5;
}
else document.getElementById("week14").style.visibility="hidden";
if(week >= 15){
document.getElementById("week15").style.visibility="visible";
ecTotal += parseFloat(document.getElementById("ec15").value || 0);
var att = parseFloat(document.getElementById("att15").value || 0);
if(attTotal >= 30)
  attTotal += att/2;
else{
  while(att > 0 && attTotal < 30){
    attTotal++;
    att--;
  }
  attTotal += att;
}
//no homework week 15
//no advanced homework week 15
}
else document.getElementById("week15").style.visibility="hidden";

document.getElementById("attTot").value=attTotal;
document.getElementById("hwTot").value=hwTotal;
document.getElementById("advTot").value=advTotal;
document.getElementById("ecTot").value=ecTotal;

var points = (attTotal+hwTotal+advTotal+ecTotal);
document.getElementById("numPoints").value=points;
if(points > 100) document.getElementById("curGrade").value="A+";
else if(points >= 93) document.getElementById("curGrade").value="A";
else if(points >= 90) document.getElementById("curGrade").value="A-";
else if(points >= 86.7) document.getElementById("curGrade").value="B+";
else if(points >= 83.3) document.getElementById("curGrade").value="B";
else if(points >= 80) document.getElementById("curGrade").value="B-";
else if(points >= 76.7) document.getElementById("curGrade").value="C+";
else if(points >= 73.3) document.getElementById("curGrade").value="C";
else if(points >= 70) document.getElementById("curGrade").value="C-";
else if(points >= 66.7) document.getElementById("curGrade").value="D+";
else if(points >= 63.3) document.getElementById("curGrade").value="D";
else if(points >= 60) document.getElementById("curGrade").value="D-";
else document.getElementById("curGrade").value="F";

var predictedPoints = 0;
if(week > 7) predictedPoints = (points/(week-2))*12
else if(week > 0) predictedPoints = (points/week)*12;
document.getElementById("predPoints").value=predictedPoints;

if(predictedPoints > 100) document.getElementById("predGrade").value="A+";
else if(predictedPoints >= 93) document.getElementById("predGrade").value="A";
else if(predictedPoints >= 90) document.getElementById("predGrade").value="A-";
else if(predictedPoints >= 86.7) document.getElementById("predGrade").value="B+";
else if(predictedPoints >= 83.3) document.getElementById("predGrade").value="B";
else if(predictedPoints >= 80) document.getElementById("predGrade").value="B-";
else if(predictedPoints >= 76.7) document.getElementById("predGrade").value="C+";
else if(predictedPoints >= 73.3) document.getElementById("predGrade").value="C";
else if(predictedPoints >= 70) document.getElementById("predGrade").value="C-";
else if(predictedPoints >= 66.7) document.getElementById("predGrade").value="D+";
else if(predictedPoints >= 63.3) document.getElementById("predGrade").value="D";
else if(predictedPoints >= 60) document.getElementById("predGrade").value="D-";
else document.getElementById("predGrade").value="F";

/* TODO:
  - calculate best possible grade
*/
}
