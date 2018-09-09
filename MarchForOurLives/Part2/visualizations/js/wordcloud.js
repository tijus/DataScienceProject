var fill = d3.scale.category20();

var layout;

function wordCloud(fileName){
  var datascale = d3.scale.linear().range([20,100]);
  d3.tsv(fileName,function(data) {
    //console.log(data);
    data = data.slice(0,60);
    var dataset = data
        //.filter(function(d){return{text: d.Count>500}})
        .map(function(d){ return{text: d.Word, size:+d.Count}; })
        .sort(function(a,b) { return d3.descending(a.size, b.size); })
        datascale.domain([
            d3.min(dataset,function(d){
              return d.size;
            }),
            d3.max(dataset,function(d){
              return d.size;
            }),
          ]);


  layout = d3.layout.cloud()
      .size([500, 500])
      .words(dataset)
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return datascale(d.size) })
      .on("end", draw);

  layout.start();
  });
}


function articles(){
  var datascale = d3.scale.linear().range([20,100]);
  d3.tsv("nyt.tsv",function(data) {
    //console.log(data);
    data = data.slice(1,100);
    var dataset = data
        //.filter(function(d){return{text: d.Count>500}})
        .map(function(d){ return{text: d.Word, size:+d.Count}; })
        .sort(function(a,b) { return d3.descending(a.size, b.size); })

      console.log(dataset)

        datascale.domain([
            d3.min(dataset,function(d){
              return d.size;
            }),
            d3.max(dataset,function(d){
              return d.size;
            }),
          ]);


  layout = d3.layout.cloud()
      .size([500, 500])
      .words(dataset)
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return datascale(d.size) })
      .on("end", draw);

  layout.start();
  });
}


function draw(words) {
  d3.select("#word-count").append("svg")
      .attr("width", layout.size()[0])
      .attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
}