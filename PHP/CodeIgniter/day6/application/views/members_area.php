<h2>Welcome Back, <?php echo $this->session->userdata('username'); ?>!</h2>
<p>This section represents the area that only logged in members can access.</p>
<h4><?php echo anchor('login/logout', 'Logout'); ?></h4>
<?php $this->load->view('includes/info'); ?>