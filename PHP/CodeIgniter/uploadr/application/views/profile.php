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

                <img alt="logo" id="logo" src="<?php echo base_url() ?>images/logo.png" /> <h1>: Profile</h1>

                <div id="boxtop"></div>

                <div id="boxmid">

                    <?php foreach ($files as $file): ?>

                        <div class="section">
                            <span><?php echo $file->name ?></span>
                            <div style="float: right;">
                                <span><?php echo anchor("files/$file->name", "View"); ?></span>
                                <span><?php echo anchor("profile/delete/$file->id", "Delete"); ?></span>
                            </div>
                        </div>

                    <?php endforeach; ?>

                    </div>

                    <div id="boxbot"></div>

                    <div class="text" style="float: left;">
                        <p>Before uploading, check out</p>
                        <p>the <a href=#>Terms of Service</a>.</p>
                    </div>
                    <div class="text" style="float: right;">
                    <?php echo anchor('login/logout', 'Logout', 'class="submit red"'); ?>
                    <?php echo anchor('profile/upload', 'Upload', 'class="submit"'); ?>

                </div>
                <br style="clear:both; height: 0px;" />

            </div>
            <div id="bottom"></div>
        </div>
    </body>
</html>