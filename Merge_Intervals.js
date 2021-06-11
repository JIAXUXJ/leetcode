/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
  var res = [];
  intervals.sort((a, b) => a[0] - b[0]);
  if(intervals.length === 1) {
    res = intervals;
    return res;
  }
  for(var i = 0; i < intervals.length - 1; i++) {

    if(intervals[i][1] >= intervals[i+1][0]) {
      if(res.length > 0) {
        res.pop();
      }
      if(intervals[i][1] >= intervals[i+1][1]) {
        res.push([intervals[i][0], intervals[i][1]]);
        intervals[i + 1] = [intervals[i][0], intervals[i][1]];
      }else {
        res.push([intervals[i][0], intervals[i+1][1]]);
        intervals[i + 1] = ([intervals[i][0], intervals[i+1][1]]);
      }
    } else {
      if(i === 0) {
        res.push([intervals[i][0], intervals[i][1]])
      }
      res.push([intervals[i+1][0], intervals[i+1][1]]);
    }
    console.log(intervals, "/////", res)
  }
  console.log(res);
  return res;
};