# Train set
$trainImages = ".\datasets\combined\train\images"
$trainLabels = ".\datasets\combined\train\labels"

# Create labels folder if missing
if (-not (Test-Path $trainLabels)) { mkdir $trainLabels }

$images = Get-ChildItem $trainImages -File | Sort-Object Name
$labels = Get-ChildItem $trainLabels -File | Sort-Object Name

for ($i=0; $i -lt $images.Count; $i++) {
    # Rename image
    $newImageName = "img{0:D4}.jpg" -f ($i+1)
    Rename-Item -LiteralPath $images[$i].FullName -NewName $newImageName -Force

    # Rename corresponding label
    if ($i -lt $labels.Count) {
        $newLabelName = "img{0:D4}.txt" -f ($i+1)
        Rename-Item -LiteralPath $labels[$i].FullName -NewName $newLabelName -Force
    }
}

# Val set
$valImages = ".\datasets\combined\val\images"
$valLabels = ".\datasets\combined\val\labels"

if (-not (Test-Path $valLabels)) { mkdir $valLabels }

$images = Get-ChildItem $valImages -File | Sort-Object Name
$labels = Get-ChildItem $valLabels -File | Sort-Object Name

for ($i=0; $i -lt $images.Count; $i++) {
    # Rename image
    $newImageName = "val{0:D4}.jpg" -f ($i+1)
    Rename-Item -LiteralPath $images[$i].FullName -NewName $newImageName -Force

    # Rename corresponding label
    if ($i -lt $labels.Count) {
        $newLabelName = "val{0:D4}.txt" -f ($i+1)
        Rename-Item -LiteralPath $labels[$i].FullName -NewName $newLabelName -Force
    }
}

Write-Host "✅ Images and labels for train and val renamed safely."
