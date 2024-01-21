function load_text(src,dest) 
    {
      var file = new XMLHttpRequest();
      file.open("GET", src, false);
      file.send();

      if (file.status === 200) 
      {  // Makes sure it's found the file
        text = file.responseText;
        document.getElementById(dest).innerHTML = text;

        // Add a new entry to the history stack
      //  window.history.pushState({src: src, dest: dest}, '', '?src=' + encodeURIComponent(src));
      }
    }

    // Listen for back/forward navigation
    // window.onpopstate = function(event) {
    //   if (event.state) {
    //     // Re-load the text without adding a new history entry
    //     load_text(event.state.src, event.state.dest);
    //   }
    // };

function show_text(text,dest) 
{
    document.getElementById(dest).innerHTML = text;
}

function load_table(dest)
{
    load_text('https://imaginglectures.github.io/Quantitative-Big-Imaging-2024/pages/weeklyplan.txt',dest);

    const url = 'https://imaginglectures.github.io/Quantitative-Big-Imaging-2024/pages/weeklyplan.json';

    fetch(url)
      .then(response => response.json())
      .then(data => {
    const tbody = document.getElementById('weeklyTable').getElementsByTagName('tbody')[0];

    data.forEach(item => 
    {
      const row = tbody.insertRow();

      const cellIndex = row.insertCell();
      const cellIcon = row.insertCell();
      const cellTitle = row.insertCell();
      const cellDate = row.insertCell();
      const cellNotebook = row.insertCell();
      const cellSlides = row.insertCell();
      const cellPdf = row.insertCell();
      const cellVideos = row.insertCell();
      const cellExercises = row.insertCell();

      cellIndex.textContent = item.index;
      cellIcon.innerHTML = "<img src='"+item.icon+"' alt='Part 2' height='40px'/>";
      item.notebook.forEach(notebook => {
        cellNotebook.innerHTML += "<a href='https://nbviewer.jupyter.org/github/"+notebook.link+"' target='_blank'><img src='https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg' alt='"+notebook.label+"' height='30px' /></a>&nbsp;&nbsp;";
        cellSlides.innerHTML   += "<a href='https://nbviewer.jupyter.org/format/slides/github/"+notebook.link+"' target='_blank'><img src='figures/np_presentation.svg' alt='"+notebook.label+"' height='30px' /></a>&nbsp;&nbsp;";
      });
      cellTitle.textContent = item.title;
      cellDate.textContent = item.date;
      if (item.pdf != "")
        cellPdf.innerHTML = "<a href='"+item.pdf+"'><img src='figures/np_pdf_749513_FF0000.svg' height='40px' />";

      item.videos.forEach(video => {
        cellVideos.innerHTML += "<a href='"+video.link+"' target='_blank'><img src='"+video.icon+"'' alt='"+video.label+"' height='30px' /></a>&nbsp;&nbsp;";
      }); 
      
      if (item.exercises != "")
        cellExercises.innerHTML = "<a href='"+item.exercises+"''><img src='figures/np_work-from-home_3742622_000000.svg' height='40px' /></a>";
      ;
    });
  })
  .catch(error => console.error('Error:', error));
}