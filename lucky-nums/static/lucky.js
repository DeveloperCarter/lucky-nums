/** processForm: get data from form and make AJAX call to our API. */

function processForm(evt) {
    evt.preventDefault();
    let name = $('#name')
    let year = $('#year')
    let color = $('#color')
    let email = $('#email')
    await axios.post("http://127.0.0.1:5000/api/get-lucky-num", { name=name, email=email, year=year, color=color });
}
function getErrors(errors) {
  return errors;
}
/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {}

$("#lucky-form").on("submit", processForm);
