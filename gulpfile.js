/*eslint-env node*/
var gulp = require('gulp');
var livereload = require('gulp-livereload');
var plumber = require('gulp-plumber');
var path = require('path');

gulp.task('watch', function () {
  livereload.listen();

  gulp.watch(
    [
      'bvspca/**/*.html',
      'bvspca/**/*.py',
      'bvspca/static/dist/*',
    ],
    { awaitWriteFinish: true },
    function (event) {
      gulp.src(event.path)
        .pipe(plumber())
        .pipe(livereload());
    });
});


gulp.task('default', ['watch']);
