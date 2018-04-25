const NAV_VISIBLE_CLASS = 'nav-visible';
const SEARCH_VISIBLE_CLASS = 'search-visible';


/* Navigation */
function deactivateMainNavParentLinks() {
  const mainNavParentItems = Array.from(document.getElementsByClassName('main-nav__parent'));
  mainNavParentItems.forEach((parentNavItem) => {
    parentNavItem.classList.add('disabled');
    parentNavItem.href = '';
    parentNavItem.addEventListener('click', (event) => {
      event.preventDefault();
    });
  });
}

function onFirstTouch() {
  // detect if the user is touching
  // https://codeburst.io/the-only-way-to-detect-touch-with-javascript-7791a3346685
  // alert('touch5');
  document.body.classList.add('user-is-touching');
  const width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // deactivate parent nav links if touch device and full navigation
  if (width >= 850) {
    deactivateMainNavParentLinks();
  }
  window.removeEventListener('touchstart', onFirstTouch, false);
}

window.addEventListener('touchstart', onFirstTouch, false);


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
  searchButton.addEventListener('click', () => {
    if (searchText.value !== '') {
      searchBlock.submit();
    }
    searchBlock.classList.add('search-block--active');
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
