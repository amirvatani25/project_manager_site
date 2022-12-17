
//get search form and get link
let searchForm = document.getElementById('searchForm')
let pageLink = document.getElementsByClassName('page-link')

//ebsure search form exist
if(searchForm){
    for (let i=0;pageLink.length>i;i++){
        pageLink[i].addEventListener('click', function (e){
            e.preventDefault()

            //get the data att.
            let  page = this.dataset.page
            //add hidden searcj input to form
            searchForm.innerHTML +=`<input value=${page} name="page" hidden/>`

            // submit form
            searchForm.submit()
        })
    }

}

