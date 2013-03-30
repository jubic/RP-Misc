<html>
    <head>
        <?php echo link_tag('styles.css'); ?>
        <title>Uploadr</title>
    </head>
    <body>
        <div id="main">
            <img alt="beta" id="beta" src="<?php echo base_url() ?>images/beta.png" />
            <div id="top"></div>
            <div id="middle">

                <img alt="logo "id="logo" src="<?php echo base_url() ?>images/logo.png" /> <h1>: Login</h1>

                <?php echo form_open('login/go'); ?>
                <div id="boxtop"></div>

                <div id="boxmid">
                    <div class="section">
                        <span><?php echo form_label('Username:', 'username'); ?></span>
                        <?php echo form_input('username', 'Username'); ?>
                    </div>

                    <div class="section">
                        <span><?php echo form_label('Password:', 'password'); ?></span>
                        <?php echo form_password('password', 'Password'); ?>
                    </div>

                </div>

                <div id="boxbot"></div>

                <div class="text" style="float: left;">
                    <?php echo validation_errors('<p class="error">'); ?>
                    <p>Haven't got an account? Want one?</p>
                    <p><?php echo anchor('login/register', 'Register'); ?>.</p>
                </div>
                <div class="text" style="float: right;">
                    <?php echo form_submit('login', 'Login','class="submit"'); ?>
                </div>

                <?php echo form_close(); ?>
                <br style="clear:both; height: 0px;" />
            </div>
            <div id="bottom"></div>
        </div>
    </body>
</html>