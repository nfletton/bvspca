const NAV_VISIBLE_CLASS = 'nav-visible';

/* Navigation */
document.getElementById('main-nav-toggle').addEventListener('click', () => {
  const bodyClasses = document.body.classList;
  if (bodyClasses.contains(NAV_VISIBLE_CLASS)) {
    bodyClasses.remove(NAV_VISIBLE_CLASS);
  } else {
    bodyClasses.add(NAV_VISIBLE_CLASS);
  }
}, false);

document.getElementById('main-nav').addEventListener('click', (event) => {
  // Prevent events propagating above the navigation element
  event.stopPropagation();
}, false);

document.getElementsByTagName('body')[0].addEventListener('click', () => {
  // Make sure the navigation is closed when area outside navigation is clicked
  const bodyClasses = document.body.classList;
  if (bodyClasses.contains(NAV_VISIBLE_CLASS)) {
    bodyClasses.remove(NAV_VISIBLE_CLASS);
  }
}, false);


/* Site search */
const searchBlock = document.getElementById('search-block');
const searchButton = document.getElementById('search-button');
const searchText = document.getElementById('search-text');

if (searchBlock) {
  searchBlock.addEventListener('click', (e) => {
    if (e.target.id === 'search-button' && searchText.value !== '') {
      searchBlock.submit();
    }
    searchBlock.classList.add('search-block--active');
    searchButton.src = '/static/svg/search-icon-green.svg';
    searchText.placeholder = '';
    searchText.focus();
  });
}
