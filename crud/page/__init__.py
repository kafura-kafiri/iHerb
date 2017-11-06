from flask import Blueprint, request, jsonify, render_template
from config import pages
from crud import crud

skeleton = {
    'name': "",
    'html': '',
}

blue = Blueprint('page', __name__, template_folder='templates')
crud(blue, pages, template='page/index', skeleton=skeleton)

html='''

<div class="ui container">
  <h3 class="ui top attached header">
  Top Attached
</h3>
<div class="ui attached segment">
  <p></p>
</div>
<h3 class="ui attached header">
  Attached
</h3>
<div class="ui attached segment">
  <p></p>
</div>
<h3 class="ui bottom attached header">
  Bottom Attached
</h3>
</div>

'''