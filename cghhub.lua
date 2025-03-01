local keySystem = {
    ["xhahavakiagwv"] = true, -- Key hợp lệ
    ["xhahavakiagwn"] = true, -- Key hợp lệ khác
}

local function checkKey(inputKey)
    return keySystem[inputKey] or false
end

local function createUI()
    local ScreenGui = Instance.new("ScreenGui")
    local Frame = Instance.new("Frame")
    local TextBox = Instance.new("TextBox")
    local Button = Instance.new("TextButton")
    local Title = Instance.new("TextLabel")
    local GetKeyButton = Instance.new("TextButton")
    local KeyLabel = Instance.new("TextLabel")

    ScreenGui.Parent = game.CoreGui
    Frame.Parent = ScreenGui
    Frame.BackgroundColor3 = Color3.fromRGB(25, 25, 25)
    Frame.Size = UDim2.new(0, 300, 0, 250)  -- Thêm không gian cho nút Get Key
    Frame.Position = UDim2.new(0.5, -150, 0.5, -125)
    Frame.BorderSizePixel = 2
    Frame.BorderColor3 = Color3.fromRGB(0, 255, 127)

    Title.Parent = Frame
    Title.Text = "SCRIPT BY CGH"
    Title.Size = UDim2.new(1, 0, 0.2, 0)
    Title.TextSize = 18
    Title.TextColor3 = Color3.fromRGB(255, 255, 255)
    Title.BackgroundTransparency = 1

    TextBox.Parent = Frame
    TextBox.Size = UDim2.new(0.8, 0, 0.2, 0)
    TextBox.Position = UDim2.new(0.1, 0, 0.3, 0)
    TextBox.PlaceholderText = "Nhập key vào đây..."
    TextBox.Text = ""
    TextBox.TextSize = 16
    TextBox.BackgroundColor3 = Color3.fromRGB(40, 40, 40)
    TextBox.TextColor3 = Color3.fromRGB(255, 255, 255)

    Button.Parent = Frame
    Button.Size = UDim2.new(0.6, 0, 0.2, 0)
    Button.Position = UDim2.new(0.2, 0, 0.6, 0)
    Button.Text = "Xác nhận"
    Button.TextSize = 16
    Button.BackgroundColor3 = Color3.fromRGB(0, 200, 127)
    Button.TextColor3 = Color3.fromRGB(255, 255, 255)

    -- Nút "Get Key"
    GetKeyButton.Parent = Frame
    GetKeyButton.Size = UDim2.new(0.6, 0, 0.2, 0)
    GetKeyButton.Position = UDim2.new(0.2, 0, 0.8, 0)
    GetKeyButton.Text = "Get Key"
    GetKeyButton.TextSize = 16
    GetKeyButton.BackgroundColor3 = Color3.fromRGB(0, 100, 255)
    GetKeyButton.TextColor3 = Color3.fromRGB(255, 255, 255)

    -- Nhãn hiển thị key
    KeyLabel.Parent = Frame
    KeyLabel.Text = "Current Key: huy50"
    KeyLabel.Size = UDim2.new(1, 0, 0.2, 0)
    KeyLabel.Position = UDim2.new(0, 0, 0.5, 0)
    KeyLabel.TextSize = 16
    KeyLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
    KeyLabel.BackgroundTransparency = 1

    -- Xử lý nút Get Key để sao chép link lấy key
    GetKeyButton.MouseButton1Click:Connect(function()
        local keyLink = "https://huyhahack.github.io/Step-1/"  -- Thay bằng link thực tế lấy key của bạn
        setclipboard(keyLink)  -- Sao chép link vào clipboard
        KeyLabel.Text = "Link lấy key đã được sao chép!"  -- Cập nhật thông báo cho người dùng
    end)

    Button.MouseButton1Click:Connect(function()
        local key = TextBox.Text
        if checkKey(key) then
            ScreenGui:Destroy()
            loadstring(game:HttpGet("https://raw.githubusercontent.com/wpisstestfprg/Volcano/refs/heads/main/VolcanoNewUpdated.luau"))()
            
            -- Bắt đầu đếm 30 phút
            local startTime = tick()
            task.spawn(function()
                while task.wait(1) do
                    if tick() - startTime >= 86400 then  -- 30 phút
                        game.Players.LocalPlayer:Kick("Key đã hết hạn! Vui lòng nhập lại key mới.")
                        break
                    end
                end
            end)
        else
            Title.Text = "Key sai! Nhập lại."
            Title.TextColor3 = Color3.fromRGB(255, 0, 0)
        end
    end)
end

createUI()
