const teamMembers = Array.from(document.getElementsByClassName('team-member'));

function clearPopUp(e, overlay, bioContentBlocks) {
  overlay.classList.add('team-overlay--hidden');
  e.stopPropagation();
  bioContentBlocks.forEach((contentBlock) => {
    contentBlock.classList.add('team-member__bio--hidden');
  });
}

if (teamMembers) {
  const bioContentBlocks = Array.from(document.getElementsByClassName('team-member__bio'));
  const overlay = document.getElementById('team-overlay');

  bioContentBlocks.forEach((contentBlock) => {
    contentBlock.addEventListener('click', e => clearPopUp(e, overlay, bioContentBlocks));
  });

  overlay.addEventListener('click', e => clearPopUp(e, overlay, bioContentBlocks));

  teamMembers.forEach((teamMember) => {
    teamMember.addEventListener('click', () => {
      const memberKey = teamMember.dataset.key;
      document.getElementById(`bio-${memberKey}`).classList.remove('team-member__bio--hidden');
      overlay.classList.remove('team-overlay--hidden');
      return false;
    });
  });
}
