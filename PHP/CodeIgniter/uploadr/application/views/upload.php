<html>
    <head>
        <link rel="stylesheet" href="<?= base_url() ?>styles.css" type="text/css" charset="utf-8">
        <?php echo link_tag('styles.css'); ?>
        <title>Uploadr</title>
    </head>
    <body>
        <div id="main">
            <img alt="beta" id="beta" src="<?php echo base_url() ?>images/beta.png" />
            <div id="top"></div>
            <div id="middle">

                <img alt="logo" id="logo" src="<?php echo base_url() ?>images/logo.png" /> <h1>: Upload</h1>
                <?php echo form_open_multipart('profile/upload'); ?>
                <div id="boxtop"></div>

                <div id="boxmid">
                    <div class="section">
                        <span><?php echo form_label('File:', 'file'); ?></span>

                        <input type="file" name="file" />
                    </div>
                </div>

                <div id="boxbot"></div>

                <div class="text" style="float: left;">
                    <p>Before uploading, check out</p>
                    <p>the <?php echo anchor('#', 'Terms of Service');?>.</p></div>
                <div class="text" style="float: right;">
                    <?php echo form_submit('upload', 'Upload', 'class="submit"');?>
                </div>
                <?php echo form_close(); ?>
                <br style="clear:both; height: 0px;" />
            </div>
            <div id="bottom"></div>
        </div>
    </body>
</html>