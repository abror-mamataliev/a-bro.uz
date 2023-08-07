const aboutPageLoader = (urls) => {
  fetch(urls.skillsUrl)
    .then(response => response.json())
    .then(data => {
      let skillsRowElement = document.querySelector('.skills .row')
      skillsRowElement.innerHTML = ''
      data.forEach(item => {
        let children = document.createElement('div')
        children.setAttribute('role', "progressbar")
        let newSkillElement = document.createElement('div')
        newSkillElement.classList.add('col-lg-6')
        newSkillElement.appendChild(children)
        skillsRowElement.appendChild(newSkillElement)
      });
    })
}
