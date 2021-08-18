/* eslint-env node */
const { parallel, watch, src } = require('gulp');
const livereload = require('gulp-livereload');

function reloadClientSideChange(cb) {
  const watchPath = 'bvspca/static/dist/*';
  livereload.listen();

  watch(
    watchPath,
    { delay: 0 },
    () => src(watchPath).pipe(livereload()),
  );
  cb();
}

function reloadServerSideChange(cb) {
  const watchPath = ['bvspca/**/*.html', 'bvspca/**/*.pyc'];
  livereload.listen();

  watch(
    watchPath,
    { delay: 300 },
    () => src(watchPath).pipe(livereload()),
  );
  cb();
}

exports.default = parallel(reloadClientSideChange, reloadServerSideChange);
