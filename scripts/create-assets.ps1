$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$assetDirectory = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../assets'))
# Original pitch diagram: native drawing, no third-party artwork.
$bitmap = [Drawing.Bitmap]::new(1280, 720)
$canvas = [Drawing.Graphics]::FromImage($bitmap)
$canvas.SmoothingMode = 'AntiAlias'
$canvas.TextRenderingHint = 'AntiAliasGridFit'
$canvas.Clear([Drawing.ColorTranslator]::FromHtml('#f2f6f8'))
$ink = [Drawing.SolidBrush]::new([Drawing.ColorTranslator]::FromHtml('#103f63'))
$font = [Drawing.Font]::new('Arial', 30)
$small = [Drawing.Font]::new('Arial', 19)
$canvas.DrawString('Four Mandarin tones', $font, $ink, 65, 48)
$labels = @('1  High and level', '2  Rising', '3  Low and dipping', '4  Falling')
$colors = @('#bc492f', '#997000', '#117d78', '#7761a9')
for ($i = 0; $i -lt 4; $i++) {
    $x = 65 + 305 * $i
    $canvas.FillRectangle([Drawing.Brushes]::White, $x, 145, 270, 420)
    $grid = [Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml('#dce4e9'), 2)
    foreach ($y in @(245, 340, 435)) { $canvas.DrawLine($grid, $x+25, $y, $x+245, $y) }
    $pen = [Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml($colors[$i]), 9)
    $pen.StartCap = 'Round'; $pen.EndCap = 'Round'
    switch ($i) {
        0 { $canvas.DrawLine($pen, $x+25, 245, $x+245, 245) }
        1 { $canvas.DrawLine($pen, $x+25, 355, $x+245, 245) }
        2 { $canvas.DrawBezier($pen, $x+25, 365, $x+135, 505, $x+145, 445, $x+245, 285) }
        3 { $canvas.DrawLine($pen, $x+25, 245, $x+245, 435) }
    }
    $canvas.DrawString($labels[$i], $small, $ink, $x+12, 490)
    $pen.Dispose(); $grid.Dispose()
}
$canvas.DrawString('Relative pitch in isolation. In connected speech, tone 3 often stays low.', $small, $ink, 65, 620)
$bitmap.Save((Join-Path $assetDirectory 'mandarin-tones.png'), [Drawing.Imaging.ImageFormat]::Png)
$canvas.Dispose(); $bitmap.Dispose(); $font.Dispose(); $small.Dispose(); $ink.Dispose()
$icon = [Drawing.Bitmap]::new(96, 96)
$canvas = [Drawing.Graphics]::FromImage($icon)
$canvas.SmoothingMode = 'AntiAlias'
$canvas.Clear([Drawing.ColorTranslator]::FromHtml('#103f63'))
$pen = [Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml('#ffd249'), 10)
$pen.StartCap = 'Round'; $pen.EndCap = 'Round'
$canvas.DrawLine($pen, 20, 65, 49, 35)
$canvas.DrawLine($pen, 49, 35, 76, 35)
$icon.Save((Join-Path $assetDirectory 'favicon.png'), [Drawing.Imaging.ImageFormat]::Png)
$pen.Dispose(); $canvas.Dispose(); $icon.Dispose()
# JPEG suits the photographic book cover and reduces transfer size.
$cover = [Drawing.Image]::FromFile((Join-Path $assetDirectory 'ebook-cover.png'))
$cover.Save((Join-Path $assetDirectory 'ebook-cover.jpg'), [Drawing.Imaging.ImageFormat]::Jpeg)
$cover.Dispose()
