const NAV_VISIBLE_CLASS = 'nav-visible';
const SEARCH_VISIBLE_CLASS = 'search-visible';


/* Navigation */
document.getElementById('main-nav-toggle').addEventListener('click', (event) => {
  const bodyClasses = document.body.classList;
  if (bodyClasses.contains(NAV_VISIBLE_CLASS)) {
    bodyClasses.remove(NAV_VISIBLE_CLASS);
  } else {
    bodyClasses.add(NAV_VISIBLE_CLASS);
    bodyClasses.remove(SEARCH_VISIBLE_CLASS);
  }
  event.stopPropagation();
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
const headerSearchButton = document.getElementById('header-button-search');
const mobileSearchButton = document.getElementById('main-nav-mobile-search');

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

function toggleSearchDisplay() {
  const bodyClasses = document.body.classList;
  if (bodyClasses.contains(SEARCH_VISIBLE_CLASS)) {
    bodyClasses.remove(SEARCH_VISIBLE_CLASS);
  } else {
    bodyClasses.add(SEARCH_VISIBLE_CLASS);
    bodyClasses.remove(NAV_VISIBLE_CLASS);
    // set focus on search and ensure cursor is at the end of the search string
    const searchString = searchText.value;
    searchText.value = '';
    searchText.focus();
    searchText.value = searchString;
  }
}

if (headerSearchButton) {
  headerSearchButton.addEventListener('click', toggleSearchDisplay);
}

if (mobileSearchButton) {
  mobileSearchButton.addEventListener('click', toggleSearchDisplay);
}
